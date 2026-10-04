#define _GNU_SOURCE
#include <bpf/libbpf.h>
#include <errno.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "../programs/chainstate_event.h"

static volatile sig_atomic_t stop;
static void on_signal(int sig) { (void)sig; stop = 1; }

static int handle_event(void *ctx, void *data, size_t len)
{
    (void)ctx;
    if (len < sizeof(struct chainstate_event)) return 0;
    const struct chainstate_event *e = data;
    printf("{\"ts_ns\":%llu,\"pid\":%u,\"uid\":%u,\"type\":%u,\"syscall_id\":%u,\"old_state\":%u,\"new_state\":%u,\"comm\":\"%.*s\"}\n",
           (unsigned long long)e->ts_ns, e->pid, e->uid, e->type,
           e->syscall_id, e->old_state, e->new_state,
           CHAINSTATE_COMM_LEN, e->comm);
    fflush(stdout);
    return 0;
}

static int load_one(const char *path, struct ring_buffer **rb, struct bpf_object **out_obj)
{
    struct bpf_object *obj = NULL;
    struct bpf_program *prog;
    struct bpf_map *map;
    int err;

    obj = bpf_object__open_file(path, NULL);
    if (!obj) { fprintf(stderr, "open failed: %s\n", path); return -1; }
    bpf_object__for_each_program(prog, obj) {
        bpf_program__set_autoload(prog, true);
    }
    err = bpf_object__load(obj);
    if (err) { fprintf(stderr, "load/verifier failed: %s (%d)\n", path, err); bpf_object__close(obj); return -1; }

    bpf_object__for_each_map(map, obj) {
        int fd = bpf_map__fd(map);
        if (fd >= 0) {
            struct ring_buffer *new_rb = ring_buffer__new(fd, handle_event, NULL, NULL);
            if (new_rb) *rb = new_rb;
        }
    }
    bpf_object__for_each_program(prog, obj) {
        struct bpf_link *link = bpf_program__attach(prog);
        if (!link) { fprintf(stderr, "attach failed: %s\n", path); bpf_object__close(obj); return -1; }
    }
    *out_obj = obj;
    return 0;
}

int main(int argc, char **argv)
{
    const char *dir = argc > 1 ? argv[1] : "os/ebpf/build";
    char path[512];
    struct ring_buffer *rb = NULL;
    struct bpf_object *objs[4] = {0};
    const char *names[4] = {"process_monitor.bpf.o", "syscall_monitor.bpf.o", "network_monitor.bpf.o", "filesystem_monitor.bpf.o"};

    libbpf_set_strict_mode(LIBBPF_STRICT_ALL);
    signal(SIGINT, on_signal); signal(SIGTERM, on_signal);

    for (int i = 0; i < 4; i++) {
        snprintf(path, sizeof(path), "%s/%s", dir, names[i]);
        if (load_one(path, &rb, &objs[i]) != 0) return 2;
    }

    fprintf(stderr, "CHAINSTATE eBPF monitor active; enforcement is disabled.\n");
    while (!stop) {
        int err = ring_buffer__poll(rb, 250);
        if (err < 0 && err != -EINTR) break;
    }
    ring_buffer__free(rb);
    for (int i = 0; i < 4; i++) bpf_object__close(objs[i]);
    return 0;
}

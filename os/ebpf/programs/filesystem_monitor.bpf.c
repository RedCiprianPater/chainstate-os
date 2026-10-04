#include "vmlinux.h"
#include <bpf/bpf_helpers.h>
#include "chainstate_event.h"

char LICENSE[] SEC("license") = "GPL";

struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 1 << 20);
} events SEC(".maps");

SEC("tracepoint/syscalls/sys_enter_openat")
int on_openat(void *ctx)
{
    struct chainstate_event *e;
    e = bpf_ringbuf_reserve(&events, sizeof(*e), 0);
    if (!e) return 0;
    e->ts_ns = bpf_ktime_get_ns();
    e->pid = (__u32)(bpf_get_current_pid_tgid() >> 32);
    e->uid = (__u32)bpf_get_current_uid_gid();
    e->type = CS_EVENT_FILE_OPEN;
    e->syscall_id = 257; /* openat on common Linux ABIs; telemetry only. */
    e->old_state = 0;
    e->new_state = 0;
    bpf_get_current_comm(&e->comm, sizeof(e->comm));
    bpf_ringbuf_submit(e, 0);
    return 0;
}

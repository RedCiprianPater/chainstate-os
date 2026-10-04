#include "vmlinux.h"
#include <bpf/bpf_helpers.h>
#include "chainstate_event.h"

char LICENSE[] SEC("license") = "GPL";

struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 1 << 20);
} events SEC(".maps");

SEC("tracepoint/sock/inet_sock_set_state")
int on_socket_state(struct trace_event_raw_inet_sock_set_state *ctx)
{
    struct chainstate_event *e;
    e = bpf_ringbuf_reserve(&events, sizeof(*e), 0);
    if (!e) return 0;
    e->ts_ns = bpf_ktime_get_ns();
    e->pid = (__u32)(bpf_get_current_pid_tgid() >> 32);
    e->uid = (__u32)bpf_get_current_uid_gid();
    e->type = CS_EVENT_SOCKET_STATE;
    e->syscall_id = 0;
    e->old_state = (__u32)ctx->oldstate;
    e->new_state = (__u32)ctx->newstate;
    bpf_get_current_comm(&e->comm, sizeof(e->comm));
    bpf_ringbuf_submit(e, 0);
    return 0;
}

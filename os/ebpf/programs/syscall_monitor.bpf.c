#include "vmlinux.h"
#include <bpf/bpf_helpers.h>
#include "chainstate_event.h"

char LICENSE[] SEC("license") = "GPL";

struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 1 << 20);
} events SEC(".maps");

SEC("tracepoint/raw_syscalls/sys_enter")
int on_sys_enter(struct trace_event_raw_sys_enter *ctx)
{
    struct chainstate_event *e;
    /* Sampling is intentionally conservative: record 1/16 events. */
    if ((bpf_get_prandom_u32() & 15) != 0) return 0;
    e = bpf_ringbuf_reserve(&events, sizeof(*e), 0);
    if (!e) return 0;
    e->ts_ns = bpf_ktime_get_ns();
    e->pid = (__u32)(bpf_get_current_pid_tgid() >> 32);
    e->uid = (__u32)bpf_get_current_uid_gid();
    e->type = CS_EVENT_SYSCALL;
    e->syscall_id = (__u32)ctx->id;
    e->old_state = 0;
    e->new_state = 0;
    bpf_get_current_comm(&e->comm, sizeof(e->comm));
    bpf_ringbuf_submit(e, 0);
    return 0;
}

/*
 * Reserved enforcement hook. This file intentionally contains no deny/allow
 * logic. A production LSM-BPF policy must be independently reviewed, signed,
 * tested, and enabled only through an explicit operator-controlled profile.
 */
#include "vmlinux.h"
#include <bpf/bpf_helpers.h>

char LICENSE[] SEC("license") = "GPL";

SEC("lsm/file_open")
int BPF_PROG(chainstate_file_open, struct file *file)
{
    (void)file;
    return 0;
}

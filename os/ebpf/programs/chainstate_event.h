#ifndef CHAINSTATE_EVENT_H
#define CHAINSTATE_EVENT_H

#include <linux/types.h>

#define CHAINSTATE_COMM_LEN 16

enum chainstate_event_type {
    CS_EVENT_PROCESS_EXEC = 1,
    CS_EVENT_SYSCALL = 2,
    CS_EVENT_SOCKET_STATE = 3,
    CS_EVENT_FILE_OPEN = 4,
};

struct chainstate_event {
    __u64 ts_ns;
    __u32 pid;
    __u32 uid;
    __u32 type;
    __u32 syscall_id;
    __u32 old_state;
    __u32 new_state;
    char comm[CHAINSTATE_COMM_LEN];
};

#endif

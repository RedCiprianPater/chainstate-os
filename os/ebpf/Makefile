CLANG ?= clang
BPFTOOL ?= bpftool
CC ?= cc
CFLAGS ?= -O2 -g -Wall -Wextra
BPF_CFLAGS ?= -O2 -g -target bpf -D__TARGET_ARCH_x86
LIBBPF_CFLAGS ?= $(shell pkg-config --cflags libbpf 2>/dev/null)
LIBBPF_LIBS ?= $(shell pkg-config --libs libbpf 2>/dev/null)

OUT := build
INC := include
PROGS := process_monitor syscall_monitor network_monitor filesystem_monitor

all: $(OUT)/vmlinux.h $(addprefix $(OUT)/,$(addsuffix .bpf.o,$(PROGS))) $(OUT)/chainstate-ebpf-loader

$(OUT):
	mkdir -p $(OUT)

$(INC):
	mkdir -p $(INC)

$(OUT)/vmlinux.h: | $(OUT) $(INC)
	@test -r /sys/kernel/btf/vmlinux || (echo 'ERROR: /sys/kernel/btf/vmlinux unavailable; enable kernel BTF (CONFIG_DEBUG_INFO_BTF).'; exit 1)
	$(BPFTOOL) btf dump file /sys/kernel/btf/vmlinux format c > $(OUT)/vmlinux.h
	ln -sf ../build/vmlinux.h $(INC)/vmlinux.h

$(OUT)/%.bpf.o: programs/%.bpf.c $(OUT)/vmlinux.h
	$(CLANG) $(BPF_CFLAGS) $(LIBBPF_CFLAGS) -I$(OUT) -I$(INC) -c $< -o $@

$(OUT)/chainstate-ebpf-loader: loader/chainstate_ebpf_loader.c
	$(CC) $(CFLAGS) $(LIBBPF_CFLAGS) $< -o $@ $(LIBBPF_LIBS)

clean:
	rm -rf $(OUT) $(INC)/vmlinux.h

.PHONY: all clean

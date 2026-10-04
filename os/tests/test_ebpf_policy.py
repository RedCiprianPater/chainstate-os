from chainstate_os.ebpf import parse_event, runtime_policy


def test_ai_cannot_load_or_change_ebpf():
    p = runtime_policy()
    assert p["ai_can_load_bpf"] is False
    assert p["ai_can_change_policy"] is False
    assert p["runtime_compilation"] is False
    assert p["unsigned_objects"] is False
    assert p["enforcement_default"] is False


def test_event_parser_rejects_missing_required_fields():
    try:
        parse_event('{"pid":1}')
    except ValueError:
        pass
    else:
        raise AssertionError("invalid eBPF event accepted")

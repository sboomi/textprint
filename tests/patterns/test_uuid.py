from textprint.patterns import Uuid


def test_uuids():
    uuids = {
        "123e4567-e89b-12d3-a456-426655440000": True,
        "c73bcdcc-2669-4bf6-81d3-e4ae73fb11fd": True,
        "C73BCDCC-2669-4Bf6-81d3-E4AE73FB11FD": True,
        "c73bcdcc-2669-4bf6-81d3-e4an73fb11fd": False,
        "c73bcdcc26694bf681d3e4ae73fb11fd": False,
        "definitely-not-a-uuid": False,
    }

    uuid_parser = Uuid()

    for uuid, is_act_uuid in uuids.items():
        match = uuid_parser.search(uuid)
        if is_act_uuid:
            assert len(match) == 1
            assert match[0] == uuid
        else:
            assert len(match) == 0

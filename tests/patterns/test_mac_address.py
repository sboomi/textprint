from textprint.patterns import MacAddress


def test_addresses():
    addresses = {
        "01:02:03:04:ab:cd": True,
        "definitely:not:a:mac": False,
        "01-02-03-04-ab-cd": False
    }

    mac_address_parser = MacAddress()

    for address, is_mac_address in addresses.items():
        match = mac_address_parser.search(address)
        if is_mac_address:
            assert len(match) == 1
            assert match[0] == address
        else:
            assert len(match) == 0
from textprint.patterns import PortNumber


def test_port_numbers():
    port_numbers = {"8080": True, "3000": True, "65535": True, "65536": False}

    port_number_parser = PortNumber()

    for port_number, is_valid_port_number in port_numbers.items():
        match = port_number_parser.search(port_number)
        if is_valid_port_number:
            assert len(match) == 1
            assert match[0] == port_number
        else:
            assert len(match) == 0

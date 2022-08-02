from textprint.patterns import IpAddress


def test_series_of_ipv4():
    ips = {
        "192.168.1.1": True,
        "127.0.0.1": True,
        "0.0.0.0": True,
        "255.255.255.255": True,
        "256.256.256.256": False,
        "999.999.999.999": False,
        "1.2.3": False,
        "1.2.3.4": True,
    }

    ip_address_parser = IpAddress()

    for ip, is_ip_v4 in ips.items():
        match = ip_address_parser.search(ip)
        if is_ip_v4:
            assert len(match) == 1
            assert match[0] == ip
        else:
            assert len(match) == 0


def test_series_of_ipv6():
    ips = {
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334": True,
        "FE80:0000:0000:0000:0202:B3FF:FE1E:8329": True,
        "192.168.1.1": False,
        "test:test:test:test:test:test:test:test": False,
    }

    ip_address_parser = IpAddress(is_v6=True)

    for ip, is_ip_v4 in ips.items():
        match = ip_address_parser.search(ip)
        if is_ip_v4:
            assert len(match) == 1
            assert match[0] == ip
        else:
            assert len(match) == 0

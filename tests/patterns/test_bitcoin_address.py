from textprint.patterns import BitcoinAddress


def test_is_bitcoin_address():
    """GIVEN potential addresses
    WHEN BitcoinAddress object is searching
    THEN validate full match
    """

    addresses = {
        "1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY": True,
        "loremipsum": False,
        "16ftSEQ4ctQFDtVZiUBusQUjRrGhM3JYwe": True,
        "1EBHA1ckUWzNKN7BMfDwGTx6GKEbADUozX": True,
        "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae": False,
        "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq": True,
    }

    bitcoin_parser = BitcoinAddress()
    for address, is_bitcoin_address in addresses.items():
        match = bitcoin_parser.search(address)
        if is_bitcoin_address:
            assert len(match) == 1
            assert match[0] == address
        else:
            assert len(match) == 0

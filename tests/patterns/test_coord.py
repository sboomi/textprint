from textprint.patterns import GeographicCoordinates
from textprint.patterns.coords import Point


def test_geographic_coordinates():
    """GIVEN a set of coordinates
    WHEN GeographicCoordinates is searching in the string
    THEN validate coordinates
    """

    test_coordinates = {
        "+90.0, -127.554334": True,
        "45, 180": True,
        "-90.000, -180.0": True,
        "20,80": True,
        "47.1231231, 179.99999999": True,
        "-90., -180.": False,
        "045, 180": True,
    }

    coords_parser = GeographicCoordinates()

    for coords, is_lat_lon in test_coordinates.items():
        match = coords_parser.search(coords)
        if is_lat_lon:
            assert len(match) == 1
            assert match[0] == coords
        else:
            assert len(match) == 0


def test_geographic_coordinates_with_point_objects():
    """GIVEN parsable coordinates
    WHEN GeographicCoordinates is running to_coords
    THEN return a Point(lat,lon) for each coordinate
    """

    test_coordinates = {
        "+90.0, -127.554334": Point(90.0, -127.554334),
        "45, 180": Point(45.0, 180.0),
        "-90.000, -180.0": Point(-90.0, -180.0),
        "20,80": Point(20.0, 80.0),
        "47.1231231, 179.99999999": Point(47.1231231, 179.99999999),
        "045, 180": Point(45.0, 180.0),
    }

    coords_parser = GeographicCoordinates()

    for coords, exp_point in test_coordinates.items():
        point = coords_parser.to_coords(coords)[0]
        assert point == exp_point

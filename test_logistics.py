from mylib.logistics import (
    calculate_distance,
    find_coordinates,
    calculate_total_distance,
    calculate_travel_time,
    cities_list,
)
from fastapi.testclient import TestClient
from main import app
from logisticsCli import cli
from click.testing import CliRunner


def test_calculate_distance():
    assert calculate_distance("New York", "Los Angeles") == 3944.42


def test_cities_list():
    assert "New York" in cities_list()


def test_find_coordinates():
    assert find_coordinates("New York") == (40.7128, -74.0060)
    assert find_coordinates("Los Angeles") == (34.0522, -118.2437)
    assert find_coordinates("Chicago") == (41.8781, -87.6298)
    assert find_coordinates("Houston") == (29.7604, -95.3698)
    assert find_coordinates("Phoenix") == (33.4484, -112.0740)
    assert find_coordinates("Philadelphia") == (39.9526, -75.1652)
    assert find_coordinates("San Antonio") == (29.4241, -98.4936)
    assert find_coordinates("San Diego") == (32.7157, -117.1611)
    assert find_coordinates("Dallas") == (32.7767, -96.7970)
    assert find_coordinates("San Jose") == (37.3382, -121.8863)


def test_calculate_total_distance():
    assert (
        calculate_total_distance(
            [
                "New York",
                "Los Angeles",
                "Chicago",
                "Houston",
                "Phoenix",
                "Philadelphia",
                "San Antonio",
                "San Diego",
                "Dallas",
                "San Jose",
            ]
        )
        == 21737.389999999996
    )
    assert calculate_total_distance(["New York", "Los Angeles"]) == 3944.42


def test_calculate_travel_time():
    assert calculate_travel_time("New York", "Los Angeles") == 65.74
    assert calculate_travel_time("New York", "Los Angeles", 100) == 39.44


# write test for each command in logisticsCli.py
def test_calculate_distance_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["calculate_distance", "New York", "Los Angeles"])
    assert result.exit_code == 0
    assert (
        "The distance between New York and Los Angeles is 3944.42 km" in result.output
    )


def test_cities_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["cities"])
    assert result.exit_code == 0
    assert (
        "The list of cities are ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']"
        in result.output
    )


def test_find_coordinates_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["find_coordinates", "New York"])
    assert result.exit_code == 0
    assert "The coordinates of New York are (40.7128, -74.006)" in result.output


def test_calculate_total_distance_command():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "calculate_total_distance",
            "New York",
            "Los Angeles",
            "Chicago",
            "Houston",
            "Phoenix",
            "Philadelphia",
            "San Antonio",
            "San Diego",
            "Dallas",
            "San Jose",
        ],
    )
    assert result.exit_code == 0
    assert (
        "The total distance between the cities is 21737.389999999996 km"
        in result.output
    )


# build a test for the cities endpoint
def test_cities_endpoint():
    with TestClient(app) as client:
        response = client.get("/cities")
        assert response.status_code == 200
        assert response.json() == {
            "cities": [
                "New York",
                "Los Angeles",
                "Chicago",
                "Houston",
                "Phoenix",
                "Philadelphia",
                "San Antonio",
                "San Diego",
                "Dallas",
                "San Jose",
            ]
        }


# build a test for the distance endpoint
def test_calculate_distance_post():
    with TestClient(app) as client:
        response = client.post(
            "/distance",
            json={"city1": {"name": "New York"}, "city2": {"name": "Los Angeles"}},
        )
        assert response.status_code == 200
        assert response.json() == {
            "city1": "New York",
            "city2": "Los Angeles",
            "distance": 3944.42,
        }


# build a test for the travel_time endpoint
def test_calculate_travel_time_post():
    with TestClient(app) as client:
        response = client.post(
            "/travel_time",
            json={
                "city1": {"name": "New York"},
                "city2": {"name": "Los Angeles"},
                "speed": 60,
            },
        )
        assert response.status_code == 200
        assert response.json() == {
            "city1": "New York",
            "city2": "Los Angeles",
            "speed": 60,
            "travel_time": 65.74,
        }


# Run the test with the following command:
# pytest test_logistics.py

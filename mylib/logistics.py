"""
This module deals with logistics and calculates the distance between two points,
the time it takes to travel between them, and other logistics-related questions for a given speed.
"""

from geopy import distance as geopy_distance

# Build a list of 10 cities in the USA and their coordinates
cities = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3698),
    "Phoenix": (33.4484, -112.0740),
    "Philadelphia": (39.9526, -75.1652),
    "San Antonio": (29.4241, -98.4936),
    "San Diego": (32.7157, -117.1611),
    "Dallas": (32.7767, -96.7970),
    "San Jose": (37.3382, -121.8863),
}


# Build a function that calculates the distance between two cities
def calculate_distance(city_name1, city_name2):
    return round(geopy_distance.distance(cities[city_name1], cities[city_name2]).km, 2)


def cities_list():
    return [city[0] for city in cities.items()]


# build a function that finds the coordinates(longitude and latitude) of a city
def find_coordinates(city_name):
    return cities[city_name]


find_coordinates("New York")


# Calculate the total distance between a list of cities
def calculate_total_distance(city_list):
    total_distance = 0
    for i in range(len(city_list) - 1):
        total_distance += calculate_distance(city_list[i], city_list[i + 1])
    return total_distance


# estimate the travel time between two cities in car
# assuming the average speed is 60km/h
def calculate_travel_time(city1, city2, speed=60):
    distance = calculate_distance(city1, city2)
    return round(distance / speed, 2)

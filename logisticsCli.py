#!/usr/bin/env python3
from mylib.logistics import (
    calculate_distance,
    find_coordinates,
    calculate_total_distance,
    calculate_travel_time,
    cities_list,
)
import click


# create a click command group
@click.group()
def cli():
    """logistics tools"""


@cli.command("calculate_distance")
@click.argument("city1")
@click.argument("city2")
def calculate_distance_command(city1, city2):
    """calculate the distance between two cities"""
    click.echo(
        f"The distance between {city1} and {city2} is {calculate_distance(city1, city2)} km"
    )


@cli.command("cities")
def cities():
    """list of cities
    Example:python logisticsCli.py cities"""
    click.echo(f"The list of cities are {cities_list()}")


@cli.command("find_coordinates")
@click.argument("city")
def find_coordinates_command(city):
    """find the coordinates of a city"""
    click.echo(f"The coordinates of {city} are {find_coordinates(city)}")


@cli.command("calculate_total_distance")
@click.argument("city_list", nargs=-1)
def calculate_total_distance_command(city_list):
    """calculate the total distance between a list of cities"""
    click.echo(
        f"The total distance between the cities is {calculate_total_distance(city_list)} km"
    )


@cli.command("calculate_travel_time")
@click.argument("city1")
@click.argument("city2")
@click.option("--speed", default=60, help="average speed in km/h")
def calculate_travel_time_command(city1, city2, speed):
    """calculate the travel time between two cities"""
    click.echo(
        f"The travel time between {city1} and {city2} is {calculate_travel_time(city1, city2, speed)} hours"
    )


if __name__ == "__main__":
    cli()

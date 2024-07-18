#!/usr/bin/env python3
from mylib.logistics import (
    calculate_distance,
    find_coordinates,
    calculate_total_distance,
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


if __name__ == "__main__":
    cli()

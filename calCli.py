#!/usr/bin/env python3
from mylib.calc import add, sub, mul, div, power

import click


@click.group()
def cli():
    """A calculator program"""


@cli.command("add")
@click.argument("x", type=float)
@click.argument("y", type=float)
def add_command(x, y):
    """Add two numbers
    Example:
    ./calCli.py add 2 3

    """
    result = add(x, y)
    # use color output to print the result
    click.echo(click.style(f"Result: {result}", fg="green"))


@cli.command("sub")
@click.argument("x", type=float)
@click.argument("y", type=float)
def sub_command(x, y):
    """Subtract two numbers
    Example:
    ./calCli.py sub 5 3

    """
    result = sub(x, y)
    click.echo(click.style(f"Result: {result}", fg="yellow"))


@cli.command("mul")
@click.argument("x", type=float)
@click.argument("y", type=float)
def mul_command(x, y):
    """Multiply two numbers
    Example:
    ./calCli.py mul 2 3

    """
    result = mul(x, y)
    click.echo(click.style(f"Result: {result}", fg="blue"))


@cli.command("div")
@click.argument("x", type=float)
@click.argument("y", type=float)
def div_command(x, y):
    """Divide two numbers
    Example:
    ./calCli.py div 6 3

    """
    result = div(x, y)
    click.echo(click.style(f"Result: {result}", fg="red"))


@cli.command("power")
@click.argument("x", type=float)
@click.argument("y", type=float)
def power_command(x, y):
    """Calculate the power of a number
    Example:
    ./calCli.py power 2 3

    """
    result = power(x, y)
    click.echo(click.style(f"Result: {result}", fg="magenta"))


if __name__ == "__main__":
    cli()

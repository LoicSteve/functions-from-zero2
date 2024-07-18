from mylib.calc import add, sub, mul, div, power
from calCli import cli
from click.testing import CliRunner


# write test for each command in calCli.py
def test_add_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "2", "3"])
    assert result.exit_code == 0
    assert "Result: 5.0" in result.output


def test_sub_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["sub", "5", "3"])
    assert result.exit_code == 0
    assert "Result: 2.0" in result.output


def test_mul_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["mul", "2", "3"])
    assert result.exit_code == 0
    assert "Result: 6.0" in result.output


def test_div_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["div", "6", "3"])
    assert result.exit_code == 0
    assert "Result: 2.0" in result.output


def test_power_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["power", "2", "3"])
    assert result.exit_code == 0
    assert "Result: 8.0" in result.output


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_sub():
    assert sub(2, 3) == -1
    assert sub(0, 0) == 0
    assert sub(-1, 1) == -2
    assert sub(-1, -1) == 0


def test_mul():
    assert mul(2, 3) == 6
    assert mul(0, 0) == 0
    assert mul(-1, 1) == -1
    assert mul(-1, -1) == 1


def test_div():
    assert div(6, 3) == 2
    assert div(0, 1) == 0
    assert div(-1, 1) == -1
    assert div(-1, -1) == 1


def test_power():
    assert power(2, 3) == 8
    assert power(0, 0) == 1
    assert power(-1, 1) == -1
    assert power(-1, -1) == -1

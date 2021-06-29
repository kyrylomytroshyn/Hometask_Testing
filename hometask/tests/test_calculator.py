""" Calculator module test cases """
from math import sqrt
import pytest

from hometask.calculator import Calculator

valid_ans = [
    (0, 1),
    (-10, 1),
    (10, -1),
    (-12, -1),
]

sqrt_valid_ans = [0, 1, 100]
sqrt_invalid_value_ans = [-1, -10]
sqrt_invalid_type_ans = [1.1, [1, 2], "1", {1: 1}]

invalid_ans = [
    (1.1, 0.1),
    (1.1, 10),
    (0, "1"),
    ("1", 0),
    ("13", 0.1),
    (0.1, "13"),
    (-10, 0.1),

]


@pytest.mark.parametrize('x,y', valid_ans)
def test_add_valid(x: int, y: int, calc: Calculator):
    assert calc.add(x, y) == x + y


@pytest.mark.parametrize('x,y', valid_ans)
def test_sub_valid(x, y, calc: Calculator):
    assert calc.subtract(x, y) == x - y


@pytest.mark.parametrize('x,y', valid_ans)
def test_div_valid(x, y, calc: Calculator):
    assert calc.divide(x, y) == x / y


@pytest.mark.parametrize('x,y', valid_ans)
def test_mul_valid(x, y, calc: Calculator):
    assert calc.multiply(x, y) == x * y


@pytest.mark.parametrize('x,y', valid_ans)
def test_mod_valid(x, y, calc: Calculator):
    assert calc.mod(x, y) == x % y


@pytest.mark.parametrize('x,y', valid_ans)
def test_pow_valid(x, y, calc: Calculator):
    assert calc.power(x, y) == x ** y


@pytest.mark.parametrize('x', sqrt_valid_ans)
def test_sqrt_valid(x, calc: Calculator):
    assert calc.root(x) == sqrt(x)


@pytest.mark.parametrize('x,y', invalid_ans)
def test_invalid_add(x, y, calc: Calculator):
    with pytest.raises(TypeError):
        calc.add(x, y)


@pytest.mark.parametrize('x,y', invalid_ans)
def test_invalid_mul(x, y, calc: Calculator):
    with pytest.raises(TypeError):
        calc.multiply(x, y)


@pytest.mark.parametrize('x,y', invalid_ans)
def test_invalid_sub(x, y, calc: Calculator):
    with pytest.raises(TypeError):
        calc.subtract(x, y)


@pytest.mark.parametrize('x,y', invalid_ans)
def test_invalid_div(x, y, calc: Calculator):
    with pytest.raises(TypeError):
        calc.divide(x, y)


@pytest.mark.parametrize('x,y', invalid_ans)
def test_invalid_pow(x, y, calc: Calculator):
    with pytest.raises(TypeError):
        calc.power(x, y)


# @pytest.mark.parametrize('x,y', invalid_ans)
# def test_invalid_sqrt(x, y, calc: Calculator):
#     with pytest.raises(TypeError):
#         calc.root(x)

@pytest.mark.parametrize('x', sqrt_invalid_type_ans)
def test_invalid_type_sqrt(x, calc: Calculator):
    with pytest.raises(TypeError):
        calc.root(x)


@pytest.mark.parametrize('x', sqrt_invalid_value_ans)
def test_invalid_value_sqrt(x, calc: Calculator):
    with pytest.raises(ValueError):
        calc.root(x)


@pytest.mark.parametrize('x,y', invalid_ans)
def test_invalid_mod(x, y, calc: Calculator):
    with pytest.raises(TypeError):
        calc.mod(x, y)


def test_invalid_div_zero(calc: Calculator):
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)

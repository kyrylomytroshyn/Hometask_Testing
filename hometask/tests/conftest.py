import pytest

from hometask.calculator import Calculator


@pytest.fixture
def calc() -> Calculator:
    return Calculator()

import pytest
from task_one import Numbers

def test_sum_of_numbers():
    numbers = Numbers([1, 2, 3, 4, 5])
    assert numbers.sum_of_numbers() == 15

def test_arithmetic_mean_of_numbers():
    numbers = Numbers([1, 2, 3, 4, 5])
    assert numbers.arithmetic_mean_of_numbers() == 3.0

def test_max_number():
    numbers = Numbers([1, 2, 3, 4, 5])
    assert numbers.max_number() == 5

def test_min_number():
    numbers = Numbers([1, 2, 3, 4, 5])
    assert numbers.min_number() == 1
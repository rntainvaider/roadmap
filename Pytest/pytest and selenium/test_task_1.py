from task_1 import check_age, get_cost, check_auth
import pytest


@pytest.mark.parametrize(
    "age, result",
    [
        (17, "Доступ запрещён"),
        (12, "Доступ запрещён"),
        (18, "Доступ разрешён"),
        (25, "Доступ разрешён"),
    ],
)
def test_check_age(age: int, result: str) -> None:
    assert check_age(age) == result


@pytest.mark.parametrize(
    "weight, result",
    [
        (10, "Стоимость доставки: 200 руб."),
        (8, "Стоимость доставки: 200 руб."),
        (15, "Стоимость доставки: 500 руб."),
        (20, "Стоимость доставки: 500 руб."),
    ],
)
def test_get_cost(weight: int, result: str) -> None:
    assert get_cost(weight) == result


@pytest.mark.parametrize(
    "login, password, result",
    [
        ("admin", "123", "Доступ ограничен"),
        ("user", "password", "Доступ ограничен"),
        ("admin", "password", "Добро пожаловать"),
    ],
)
def test_check_auth(login: str, password: str, result: str) -> None:
    assert check_auth(login, password) == result

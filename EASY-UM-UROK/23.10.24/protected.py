# 2. Защита: Напишите декоратор protected, который будет проверять наличие авторизации пользователя
# перед вызовом функции и поднимать исключение, если у него нет прав доступа.

authenticated_users = []
bannes_users = []
current_user = ""


def protected(func) -> None:
    def wrapper(nickname) -> None:
        if (
            nickname in authenticated_users
            and current_user == nickname
            and nickname not in bannes_users
        ):
            give_my_password(nickname)
        elif nickname not in authenticated_users and current_user != nickname:
            print("Необходимо авторизоваться")
        elif nickname in authenticated_users and current_user != nickname:
            bannes_users.append(nickname)
            print("Вы забанены")

    return wrapper


@protected
def give_my_password(nickname) -> None:
    dict = {"user1": "1234", "user2": "4567", "user3": "71265", "user4": "8877"}
    print(f"Ваш пароль: {dict[nickname]}")
    return dict[nickname]


def authintificate(nickname) -> None:
    if nickname in authenticated_users:
        authenticated_users.remove(nickname)
        current_user = ""
    else:
        authenticated_users.append(nickname)
        current_user = nickname


authintificate("user1")
give_my_password("user1")

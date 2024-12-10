def print_board(board):
    """Функция для вывода игрового поля."""
    print("\n")
    print("  0   1   2")
    print("-" * 12)
    count = 0
    for row in board:
        print(f"{count}", " | ".join(row))
        print("-" * 13)
        count += 1
    print("\n")


def check_winner(board):
    """Функция для проверки завершения игры."""
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Проверка на ничью
    for row in board:
        if " " in row:
            return None  # Игра продолжается

    return "Tie"  # Ничья


def is_valid_move(board, row, col):
    """Функция для проверки корректности ввода координат."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "


def main():
    """Основной цикл игры."""
    print("Добро пожаловать в игру Крестики-Нолики!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Ход игрока {current_player}.")

        try:
            move = input("Введите координаты (строка и столбец через пробел): ")
            row, col = map(int, move.split())
        except ValueError:
            print("Ошибка ввода! Введите два числа через пробел.")
            continue

        if not is_valid_move(board, row, col):
            print("Некорректный ход. Попробуйте снова.")
            continue

        # Выполнение хода
        board[row][col] = current_player

        # Проверка на завершение игры
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Tie":
                print("Игра закончилась вничью!")
            else:
                print(f"Игрок {winner} победил!")
            break

        # Смена игрока
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Крестики-Нолики")

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

def switch_player() -> None:
    global current_player
    current_player = "O" if current_player == "X" else "X"

def check_winner() -> str | None:
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    if all(board[row][col] != "" for row in range(3) for col in range(3)):
        return "Ничья"

    return None

def button_click(row, col) -> None:
    if board[row][col] == "" and not check_winner():
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        winner = check_winner()
        if winner:
            if winner == "Ничья":
                messagebox.showinfo("Результат", "Ничья!")
            else:
                messagebox.showinfo("Результат", f"Победитель: {winner}")
            reset_board()
        else:
            switch_player()

def reset_board() -> None:
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                           command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

root.mainloop()

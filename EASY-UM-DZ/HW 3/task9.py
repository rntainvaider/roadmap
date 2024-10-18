def reset_watch_face(run: int, number: int):
    sum_run = 0
    for num in str(run):
        sum_run += int(num)
    
    if sum_run > number:
        return "Сброс.\nПробег: 0"
    else:
        return f"Сегодня не сломался.\nПробег: {run}"

if __name__ == "__main__":
    run = int(input("Введите пробег: "))
    number = int(input("Введите сегодняшнее число: "))
    print(reset_watch_face(run, number))
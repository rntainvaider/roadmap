def entering_numbers():
    numbers = list(map(int, input("Введите 10 чисел через пробел:\n").split()))
    return numbers

def check_for_increasing(numbers):
    is_increasing = True
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            is_increasing = False
            break
    
    if is_increasing:
        print("Числа упорядочены по возрастанию.")
    else:
        print("Числа не упорядочены по возрастанию.")

check_for_increasing(entering_numbers())

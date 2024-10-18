def get_lucky_ticket(numbers: str) -> str:
    ticket_part1 = 0
    ticket_part2 = 0

    for numb in numbers[:3]:
        ticket_part1 += int(numb)

    for numb in numbers[3:]:
        ticket_part2 += int(numb)

    if ticket_part1 == ticket_part2:
        return "Счастливый билетик"
    else:
        return "Не счастливый билетик"

def get_ticket_number():
    while True:
        numbers = input("Введите номер билета: ")
        if len(numbers) != 6:
            print("Длина билета не равна 6")
            continue
        else:
            return numbers

print(get_lucky_ticket(get_ticket_number()))
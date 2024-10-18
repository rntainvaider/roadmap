def day_work():
    print("Начался 8-часовой рабочий день")
    count_hours = 1
    count_task = 0
    wife = False
    while count_hours <= 8:
        print(f"{count_hours}-й час")
        task = int(input("Сколько задач решит Максим? "))
        count_task += task
        wife_calls = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
        if wife_calls == 1:
            wife = True
        count_hours += 1

    if wife == True:
        return (f"Рабочий день закончился. Всего выполнено задач: {count_task}\n"
                "Нужно зайти в магазин.")
    else:
        return f"Рабочий день закончился. Всего выполнено задач: {count_task}"
  
print(day_work())
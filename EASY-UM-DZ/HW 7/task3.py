def game_bomb():
    timer_second = 10
    for _ in range(timer_second + 1):
        print(f"Осталось секунд {timer_second}")
        if timer_second == 0:
            print("Вы не обезвредели бомбу!!")
            break
        question = input("Хотите сейчас обезвредить бомбу? да\нет\n").lower()
        if question == "да":
            print("Вы обезвредели бомбу")
            break
        elif question == "нет":
            timer_second -= 1
        
game_bomb()

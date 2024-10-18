def get_final_kilometer():
    v = int(input("Введите скорость (км/ч): "))
    t = int(input("Введите время (ч): "))

    final_kilometer = (v * t) % 115

    return f"Вася остановится на отметке: {final_kilometer} км" 

if __name__ == "__main__":
    print(get_final_kilometer())
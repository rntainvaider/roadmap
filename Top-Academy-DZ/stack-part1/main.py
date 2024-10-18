class StringStack:
    def __init__(self, size: int) -> list:
        self.stack = []
        self.size = size

    def push(self, string):
        if len(self.stack) < self.size:
            self.stack.append(string)
        else:
            print()
            print(" " * 5 + "Стек полный")
            print()
            print("=" * 80)

    def count(self):
        return len(self.stack)
    
    def clear(self):
        self.stack = []

    def is_full(self):
        if len(self.stack) == self.size:
            print()
            print(" " * 5 + "Стек полный")
            print()
            print("=" * 80)
        else:
            print()
            print(" " * 5 + "Стек неполный")
            print()
            print("=" * 80)
    
    def is_empty(self):
        if len(self.stack) == self.size:
            print()
            print(" " * 5 + "Стек полный")
            print()
            print("=" * 80)
        else:
            print()
            print(" " * 5 + "Стек неполный")
            print()
            print("=" * 80)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print()
            print(" " * 5 + "Стек пустой")
            print()
            print("=" * 80)

    def return_string(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        

print("=" * 80)
stack_size = int(input("Введите размер стека: "))
print("=" * 80)

stack = StringStack(stack_size)

while True:
    print("1. Поместить строку в стек")
    print("2. Извлечь строку строку из стека")
    print("3. Вывести количество строк в стеке")
    print("4. Проверить пустой ли стек")
    print("5. Проверить полный ли стек")
    print("6. Очистить стек")
    print("7. Получить значение без выталкивания верхней строки из стека")
    print("0. Выход")
    print("=" * 80)

    choice = input("Выберите операцию: ")
    print("=" * 80)

    if choice == "1":
        string = input("Введите строку: ")
        print("=" * 80)
        stack.push(string)

    elif choice == "2":
        reseived_string = stack.pop()
        if reseived_string:
            print()
            print(" " * 5 + "Извлеченная строка:", reseived_string)
            print()
            print("=" * 80)

    elif choice == "3":     
        if stack.count() == 0:
            print()
            print(" " * 5 + "Стек пустой")  
            print()
            print("=" * 80)
        else:
            print()
            print(" " * 5 + "Количество строк в стеке:", stack.count())
            print()
            print("=" * 80)

    elif choice == "4":
        stack.is_empty()

    elif choice == "5":
        stack.is_full()

    elif choice == "6":
        stack.clear()
        print()
        print(" " * 5 + "Стек очищен")
        print()
        print("=" * 80)

    elif choice == "7":
        return_str = stack.return_string()
        if return_str:
            print()
            print(f"Значение вытолкнутой верхней строки: \"{return_str}\"")
            print()
            print("=" * 80)
        else:
            print()
            print(" " * 15 + "Стек пустой")
            print()
            print("=" * 80)

    elif choice == "0":
        break

    else:
        print()
        print(" " * 5 + "Некорректный выбор операции")
        print()
        print("=" * 80)

print()
print("Работа со стеком закончена")
print()
print("=" * 80)
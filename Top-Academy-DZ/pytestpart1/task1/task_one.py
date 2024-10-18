class Numbers:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def sum_of_numbers(self):
        return sum(self.numbers)
    
    def arithmetic_mean_of_numbers(self):
        return sum(self.numbers) / len(self.numbers)
    
    def max_number(self):
        return max(self.numbers)

    def min_number(self):
        return min(self.numbers)

if __name__ == "__main__":
    numbers = [num for num in range(1, 21) if num % 2 == 0]
    functional = Numbers(numbers)
    print(f"Сумма элементов набора - {functional.sum_of_numbers()}")
    print(f"Среднеарифметическое элементов набора - {functional.arithmetic_mean_of_numbers()}")
    print(f"Максимум из элементов набора - {functional.max_number()}")
    print(f"Минимум из элементов набора - {functional.min_number()}")
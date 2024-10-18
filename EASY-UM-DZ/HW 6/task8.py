def wonderful_numbers():
    for item in range(10, 100):
        one_number = item // 10
        two_number = item % 10
        proiz_numbers = one_number * two_number * 3
        if item == proiz_numbers:
            print(item)
wonderful_numbers()
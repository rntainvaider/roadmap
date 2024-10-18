def get_financial_report():
    list_sums = list()
    count_sum = 1
    while count_sum <= 4:
        for _ in range(4):
            numbers = int(input(f"Введите {count_sum} сумму: "))
            list_sums.append(numbers)
            count_sum += 1
    
    first_half_year = list_sums[0] + list_sums[1]
    second_half_tear = list_sums[2] + list_sums[3]
    result = first_half_year / second_half_tear
    return result

if __name__ == "__main__":
    print(get_financial_report())
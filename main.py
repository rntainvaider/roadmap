def compare_lists(list_1, list_2, ignore_case=False):
    return [item for item in list_1 if item not in list_2]


print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"]))

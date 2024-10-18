players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

print("Все члены команды из команды А, которые отдыхают:")
for key, value in players_dict.items():
    if value["team"] == "A" and value["status"] == "Rest":
        print(key, value)

print()
print("Все члены команды из группы B, которые тренируются:")
for key, value in players_dict.items():
    if value["team"] == "B" and value["status"] == "Training":
        print(key, value)
print()
print("Все члены команды из команды C, которые путешествуют:")
for key, value in players_dict.items():
    if value["team"] == "C" and value["status"] == "Travel":
        print(key, value)

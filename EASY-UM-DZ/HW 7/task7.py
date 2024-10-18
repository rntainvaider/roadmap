def scholarship(educational_grant: int, expenses: int):
    educational_grant *= 10
    
    for _ in range(1, 11):
        expenses *= 13 * 0.13
        print(educational_grant, expenses)
        

educational_grant = int(input("Введите стипендию: "))
expenses = int(input("Введите расходы на проживание: "))
scholarship(educational_grant, expenses)
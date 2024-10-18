class Employee:
    def __init__(self, name: str, dob: str, base_salary: int):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

class Buhgalteria(Employee):
    def calculate_net_salary(self):
        tax = self.base_salary - (self.base_salary * 0.25)
        return f"name - {self.name} , dob - {self.dob}, сумма налога - {tax}"
    
buh = Buhgalteria("Job", "17.01.2000", 25)

print(buh.calculate_net_salary())
class Number:
    def __init__(self, number:int):
        self.number = number

    def conversion_to_octal(self):
        return oct(self.number)

    def conversion_to_hexadecimal(self):
        return hex(self.number)

    def conversion_to_binary(self):
        return bin(self.number)

if __name__ == "__main__":  
    number = Number(-10)
    print(f"Перевод числа в восьмеричную систему исчисления - {number.conversion_to_octal()}")
    print(f"Перевод числа в шестнадцатеричную систему исчисления - {number.conversion_to_hexadecimal()}")
    print(f"Перевод числа в двоичную систему исчисления - {number.conversion_to_binary()}")
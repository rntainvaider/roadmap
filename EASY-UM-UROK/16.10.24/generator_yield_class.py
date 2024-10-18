class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit

    def generate_evens(self):
        for i in range(0, self.limit + 1, 2):
            yield i


for number in EvenNumbers(10).generate_evens():
    print(number)

class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration


for number in EvenNumbers(10):  # EvenNumbers(10) - генератор,
    print(number)  # __next__

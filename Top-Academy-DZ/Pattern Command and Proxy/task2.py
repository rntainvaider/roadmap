class NumberSet:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.numbers = self._load_numbers()

    def _load_numbers(self):
        with open (self.filename, 'r') as file:
            return [int(line.strip()) for line in file]
        
    def get_sum(self):
        return sum(self.numbers)
    
    def get_max(self):
        return max(self.numbers)
    
    def get_min(self):
        return min(self.numbers)
    
    def get_len(self):
        return len(self.numbers)
    
class NumberSetProxy:
    def __init__(self, filename, log_filename) -> None:
        self.number_set = NumberSet(filename)
        self.log_filename = log_filename

    def _log_access(self, operation):
        with open(self.log_filename, 'a') as log_file:
            log_file.write(f"Operation: {operation}\n")

    def get_sum(self):
        self._log_access("get_sum")
        return self.number_set.get_sum()
    
    def get_min(self):
        self._log_access("get_min")
        return self.number_set.get_min()
    
    def get_max(self):
        self._log_access("get_max")
        return self.number_set.get_max()
    
    def get_len(self):
        self._log_access("get_len")
        return self.number_set.get_len()
    

proxy = NumberSetProxy('numbers.txt', 'access.log')

print("Sum:", proxy.get_sum())
print("Max:", proxy.get_max())
print("Min:", proxy.get_min())
print("Len:", proxy.get_len())

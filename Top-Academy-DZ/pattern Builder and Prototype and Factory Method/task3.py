import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Product(Prototype):
    def __init__(self, name, price, category) -> None:
        self.name = name
        self.price = price
        self.category = category

    def __str__(self) -> str:
        return f"Product(Name: {self.name}, price: {self.price}, category: {self.category})"
    
if __name__ == "__main__":
    original_product = Product("Laptop", 1500, "Electronics")
    print(f"Original: {original_product}")

    cloned_product = original_product.clone()
    print(f"Cloned: {cloned_product}")

    cloned_product.name = "Gaming Laptop"
    cloned_product.price = 2000

    print("Modified Cloned:", cloned_product)
    print("Original after clone modification:", original_product)
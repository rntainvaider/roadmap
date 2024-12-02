class Stack:
    def __init__(self) -> None:
        self.stack = list()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Попытка просмотра пустого стека")
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)


def is_balanced(brackets):
    """
    Проверяет сбалансированность строки со скобками.

    :param brackets: строка со скобками
    :return: "Сбалансированно" или "Несбалансированно"
    """
    stack = Stack()
    pairs = {")": "(", "}": "{", "]": "["}

    for char in brackets:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


if __name__ == "__main__":
    stack = Stack()

    print(stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.size())
    print(stack.is_empty())

    # Примеры входных данных
    test_strings = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "}{",
        "{{[(])}}",
        "[[{())}]",
    ]

    for test in test_strings:
        print(f"{test}: {is_balanced(test)}")

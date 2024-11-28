class Stack:
    def __init__(self) -> None:
        self.stack = list()

    def is_empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

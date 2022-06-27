class Stack:
    def __init__(self):
        self.data = []

    def size(self) -> int:
        return len(self.data)

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def peak(self):
        return self.data[len(self.data) - 1]

    def empty(self) -> bool:
        return True if self.size() == 0 else False

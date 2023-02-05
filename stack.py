


class Stack:
    def __init__(self) -> None:
        self.head={}
    def push(self, value):
        self.head={value: value, next: self.head}

s = Stack()
s.push(6)
s.push(4)
s.push(5)
print('S:', s.head)
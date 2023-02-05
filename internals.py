import sys
import dis

class Person:
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_param(self):
        print(self.id, self.name)

    def __del__(self):
        print(self.id, self.name, "was deleted")

    a, b = 1, 2

p = Person(1, "Guido")

print(type(p), id(p), sys.getrefcount(p))

print(type(10), id(10), sys.getrefcount(10))


def add(a, b):
    c = a+ b
    return c

dis.dis(add)
from types import MethodType


class Obj:
    pass

o = Obj()
o.id = 1
o.name = "Ravi"

print(o.id, o.name)

def hello():
    print("Hello")

o.say_hello = hello


o.say_hello()
def display(self):
    print(self.id, self.name)

#~# Attach 'display' function to o as print
#~* Convince Python that display is aMethod of object o
o.print = MethodType(display, o) #~^Bind display to an instance of o
o.print()


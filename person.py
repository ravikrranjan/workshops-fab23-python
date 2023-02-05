class Person:
    ''' Person class '''

    #~* This is the initialize (not contructor)
    def __init__(self, id, name) -> None:
        self.id = id
        self.name= name
    #~! self is NOT a keyword - it is suggested (it  can be ANYTHING)
    def display(self):
        print("Self:", self)
        print(self.id, self.name)

  
p = Person(1, "Ravi")
p.display()
print(p.__dict__)

Person.display(p)

q = Person(1, "Ravi")
q.display()
print(q.__dict__)
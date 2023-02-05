

class Person:
    
    """
    class Person
    params: id (number) and name (str)
    
    """
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def print_person(self):
        '''
        method : print
        args: none
        remarks: prints id and name
        '''
        print(self.id, self.name)

p = Person(1, "Guido van Rossum")
# p.print_person()
print(p.__doc__)
print(p.print_person.__doc__)
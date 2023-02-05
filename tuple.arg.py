
#~#  tuple arguments

def tuple_var(*args):
    
    print(args)

tuple_var(1, 23, 4)


def tuple_var(**kwds):
    
    print(kwds)

tuple_var(id=1, name="Ravi")


def tuple_var(id, name):
    
    print(id, name)

tuple_var(id=1, name="Ravi") 
tuple_var(name="Ravi", id=5) 
#tuple_var(id=1, name="Ravi", id=3)  #~* SyntaxError: keyword argument repeated: id
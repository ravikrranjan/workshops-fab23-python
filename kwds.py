def sum_all(message1, message2, *args, **named):
    
    print(message1, message2, args, named)

    for item in args:
        print(item)

sum_all('my list', 'new list', 1, 2, 3, 4, id=2, name='Ravi', age=27)


def var_args(*args):
    print(args)


var_args('1', 'Guido', 66.5)


#~> used to pass the values of a dictionary as keyword arguments.

def var_args(p:any, name:any, age:int=1, *args:tuple, **kwargs:dict[str, any]):
    print(args)
    print(kwargs)

    print(age)
var_args('1', 'Guido', 66)


def var_args(**p):
    print(p)
var_args(id=2)
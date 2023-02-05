# from __future__ import print_function
def hello():
    print('Hello')

hello()

#~!increment 

def print_natural(start, stop, increment =1):
    
    while start< stop:
        start +=increment
        print(start, end=' ')
    # print('\n', start, stop, increment)
    print() #~% got to next line

print_natural(4, 15)
print("Hello")


#~! default arguments are instantiated ONCE!!
# my_list = []
# my_list.append(5)

def dragons_ahead(my_list=[]):
    my_list.append(5)
    print(my_list)


dragons_ahead()
dragons_ahead()
dragons_ahead()
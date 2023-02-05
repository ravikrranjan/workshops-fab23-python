
#~-> list comprehensions
list =[i for i in range(23)]

print(list)

is_done = True

value = 1 if is_done else 2 #* generate conditional value

print(value)

list2 = [1 if is_done else 2]

print(list2)


list3 = list + list2

print(list3)
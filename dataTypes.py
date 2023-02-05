#~% Python is dynamic language (But Not type-less)


#~* 1. bool

isMarried = True

print("isMarried", isMarried, type(isMarried))


#~* 2. int
count = 5
print("Count", count, type(count))

# 3. float

pi = 3.1415

print('pi', pi, type(pi))

# 4. complex

complex = 1.2j

print('complex', complex, type(complex))

# 5. str

name = "Guido"

print("name", name, type(name))

# 6. list 

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print(days, days[0], days[6])

print(type(days))

record = [123, "Guido", 14.234, True]
print(record)

record.remove(123)
record.append(78)
print(record)


# 7 tuple

tuple= (123, "Guido", 66.3, True)

print(tuple)

# 8. sets
lottery = {123, 13123,124124, 235345}

print(lottery)

# 9. dictionary (map or hashtable) - key:value

person = {"id":12, "Name":"Guido", "Age": '23423'}

print(person)
def generator(max=10):
    current = 0
    while current < max:
        yield current
        current +=2

    for value in generator(10):
        print(value)



i = iter(generator(10))

print(next(i))


print(next(i))


print(next(i))

print(next(i))


print(next(i))

print(next(i))
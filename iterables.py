class Seq:
    
    def __init__(self, max=10) -> None:
        self.max = max

    def __iter__(self):
        self.current = -1
        return self
    
    def __next__(self):
        self.current +=1
        if self.current < self.max:
            return self.current
        else:
            raise StopAsyncIteration
      


monkey = iter(Seq())

gorilla = iter(Seq())

print(next(monkey))

print(next(monkey))

print()

print(next(gorilla))
print(next(gorilla))
print(next(gorilla))
print(next(gorilla))

for value in range(10):
    print(value)
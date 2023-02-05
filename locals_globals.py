

def add_sub(a, b):
    
    for key, val in locals().items():
        print(key, val)
    return (a+b, a-b)
import sys

x, y = add_sub(5, 7)
print(add_sub(x, y))


print(sys.version_info)

for key, value in globals().copy().items():
    print(key, value)
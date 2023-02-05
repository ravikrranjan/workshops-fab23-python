import string

i = 0
for letter in string.ascii_letters:
    print("The letter at index %i is %s" % (i, letter))
    i += 1


def div1(x, y):
    print("%s/%s = %s" % (x, y, x/y))


div1(5, 2)
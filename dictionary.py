greats = {
    1: 'James Gosling',
    2: 'Dennis Ritchie',
    3: 'Lars Bak',
    4 : 'Bjarne Stroustrup'
}

print(greats)

greats[5]= "brendan Eich"

greats.update({1: "Guido van Rossum"})
greats.update({6: "Guido van Rossum"})

print( greats.popitem())

#~!  Exception id doesn't exist
# print(greats[10])

#~^ Return None if doesn't exist

print(greats.get(15))
print(greats)

#~!Exception index doesn't exists
# print(greats.pop(9))


print(greats.pop(2))

print(greats)
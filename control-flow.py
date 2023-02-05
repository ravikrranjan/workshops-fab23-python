# from __future__ import print_function

actual = 25

guess = 0

while guess <= actual:
    guess +=1
print('Actual:', guess)

a = 5
b = 8
#~# Zero -> False

#~! Non-Zero - true

value = a < b

if value:
    print('True')
else:

    print('False')


languages = ['C', 'C++', 'Python', 'Java']


for language in languages:
    print(language, sep= " ", end= " ")


# Dictionary

dic = [{'name': 'C'}]


for data in dic:
    print(data, sep= " ", end= " ")


print('\n')

for value in range(1, 101):
    
    print(value, end=' ', sep=', ')


print('\n')
for value in range(100, 500, 3):
    
    print(value, end=' ', sep=', ')


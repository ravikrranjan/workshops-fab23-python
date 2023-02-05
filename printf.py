id= 101
name = "Guido"
age = 66.3

print(f"id={id} name={name} age={age}")

print("id=[{0:^10d}] name=[{2:^15s}] age=[{1:6.2f}]".format(id, age, name))
print(f"id=[{id:^6d}] name=[{name:^15s}] age=[{age+10:6.2f}]")

s = "abc %d" % 4

print(type(s))
print(s)
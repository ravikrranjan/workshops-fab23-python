def outer():
    outer_var = 5
    print('outer', outer_var)

#* defined

    def inner():
      inner_var = 10
      print('inner', inner_var, outer_var)


# #* called
# inner()

    return inner


pointer = outer()
print(pointer)

pointer()
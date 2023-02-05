def outer():
    print('outer')


#* defined

    def inner():
      print('inner')


# #* called
# inner()

    return inner


pointer = outer()
print(pointer)

pointer()
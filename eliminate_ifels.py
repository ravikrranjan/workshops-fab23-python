


# def key_map(key):
    #~! Modification hell 
#     if key == 33:
#         return '{UP}'
#     elif key == 45:
#         return '{ESC}'
#     elif key == 88:
#         return '{PAGE_UP}'
#     else: 
#       return None
    

key_dict = {
    33: '{UP}',
    45: '{ESC}',
    88: '{PGDWN}',
    67: '{PGUP}'
}

def key_map(key):
    return key_dict.get(key)

print(key_map(23))



weather_dict = {
    0: 'Sub zero',
    10:'Very cold'
}



def weather_label(temp):
    print(temp)
    for value, label in weather_dict.items():
        print(label, value)
        if(temp < value):
          return label



print(weather_label(11))
# Create a Python function that accepts a string. This function should count 
# the number of Xs and the number of Os in the string. It should then return a boolean value of either True or False.

# If the count of Xs and Os are equal, then the function should return True. If 
# the count isn't the same, it should return False. If there are no Xs or Os in the string, it should also return True
#  because 0 equals 0. The string can contain any type and number of characters.

def xando(string1):
    x = 0
    o = 0
    for char in string1:
        if char.lower() == 'x':
            x += 1
        elif char.lower() == 'o':
            o += 1
        else:
            continue
    if x == o:
        return print(True)
    else:
        return print(False)

xando('oooxxx')
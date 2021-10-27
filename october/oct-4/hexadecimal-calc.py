def letter_to_num(letter):
    if letter.lower() == 'a':
        dec = 10
    elif letter.lower() == 'b':
        dec = 11
    elif letter.lower() == 'c':
        dec = 12
    elif letter.lower() == 'd':
        dec = 13
    elif letter.lower() == 'e':
        dec = 14
    elif letter.lower() == 'f':
        dec = 15
    else:
        dec = letter
    return dec
    

def hex_to_dec(hex_str):
    # This will convert a hexadecimal number string to a decimal integer.
    counter = len(hex_str) -1
    total = 0
    for char in hex_str:
        
        if char != int:
            char = letter_to_num(char)
        char = int(char)
        mult_of_16 = 16**counter
        total += char * mult_of_16
        counter -= 1
    return print(total)

hex_to_dec('1000')

def num_to_letter(num):
    if num == 10:
        letter = 'a'
    elif num == 11:
        letter = 'b'
    elif num == 12:
        letter = 'c'
    elif num == 13:
        letter = 'd'
    elif num == 14:
        letter = 'e'
    elif num == 15:
        letter = 'f'
    else:
        letter = str(num)
    return letter

def dec_to_hex(dec_val):
    my_str = ''
    decimal_value = dec_val
    while decimal_value > 0:
        print(decimal_value)
        remainder = decimal_value % 16
        print(remainder)
        remainder = num_to_letter(remainder)
        my_str += remainder
        decimal_value = decimal_value // 16
    return print(my_str[::-1])

dec_to_hex(7320)
def bin_add(bin_str_1, bin_str_2):
   max_width = max(len(bin_str_1), len(bin_str_2))
   bin_str_1 = bin_str_1.zfill(max_width)
   bin_str_2 = bin_str_2.zfill(max_width)

   output = ''
   carry = 0
   for i in reversed(range(len(bin_str_1))):
      if carry == 0:
         if bin_str_1[i] == '0' and  bin_str_2[i] == '0':
            output = output + '0'
            carry = 0
         elif bin_str_1[i] == '1' and  bin_str_2[i] == '1':
            output += '0'
            carry = 1
         else:
            output += '1'
            carry = 0
      else:
         if bin_str_1[i] == '0' and  bin_str_2[i] == '0':
            output = output + '1'
            carry = 0
         elif bin_str_1[i] == '1' and  bin_str_2[i] == '1':
            output += '1'
            carry = 1
         else:
            output += '0'
            carry = 1
   if carry == 1:
      output += '1'
   return output[::-1]


def bin_mul(bin_str_1, bin_str2):
   output = ''
   for i, ch in enumerate(reversed(bin_str2)):
      if ch == '1':
         output = bin_add(output, bin_str_1 + ('0' * i))

   return output

def bin_sub(bin_str_1, bin_str_2):
   max_length = max(len(bin_str_1), len(bin_str_2))
   bin_str_1 = bin_str_1.zfill(max_length)[::-1]
   bin_str_2 = bin_str_2.zfill(max_length)[::-1]
   output = ''
   borrow = 0

   for i in range(max_length):
      num1 = bin_str_1[i]
      num2 = bin_str_2[i]
      
      if borrow == 1:
         if num1 == '1':
            num1 = '0'
            borrow = 0
         else:
            num1 = '1'
      if num1 == num2:
         output += '0'
      elif num1 == '1':
         output += '1'
      else:
         output += '1'
         borrow = 1

   if borrow == 1:
      return "Error: Negative Result"

   return output[::-1]

def bin_div(bin_str_1, bin_str_2):
   if bin_sub(bin_str_1, bin_str_2) == "Error: Negative Result":
      return "Error: No fractions allowed"
   
   output = ''
   result = ''

   for i, ch in enumerate(bin_str_1):
      result += ch  # 1
      sub_result = bin_sub(result, bin_str_2)  # "001"
      if sub_result == "Error: Negative Result":
         output += '0'
      else:
         output += '1'
         result = sub_result
   
   return output

print(bin_div('10111010', '0010'))
# print(bin_sub('10000000', '1001000101'))


def bin_inverse(bin1):
  str1 = ''
  for char in bin1:
    if char == '1':
      str1 = str1 + '0'
    else:
      str1 = str1 + '1'
  if bin1[0] == '1':
    inverse_bin = bin_add(str1, '1')
    inverse_bin = (inverse_bin[::-1] + '1')[::-1]
  else:
    inverse_bin = str1
  return inverse_bin

bin_inverse('10111')




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
   # This will convert a decimal number string to a hexadecimal value.
    my_str = ''
    decimal_value = dec_val
    while decimal_value > 0:
        remainder = decimal_value % 16
        remainder = num_to_letter(remainder)
        my_str += remainder
        decimal_value = decimal_value // 16
    return print(my_str[::-1])








operation = input('Operation: \n(A)dd \n(S)ubtract \n(M)ultiply \n(D)ivide \n Enter answer here: ')
num1 = input('First number: ')
num2 = input('Second number: ')

if num1[0] == '1':
   num1 = bin_inverse(num1)
if num2[0] == '1':
   num2 = bin_inverse(num2)

if operation.lower() == 'm':
   print(f"Answer to multiplication is {bin_mul(num1, num2)}.")
if operation.lower() == 'a':
   print(f"Answer to addition is {bin_add(num1, num2)}.")
if operation.lower() == 's':
   print(f"Answer to subtraction is {bin_sub(num1, num2)}.")
if operation.lower() == 'd':
   print(f"Answer to division is {bin_div(num1, num2)}.")




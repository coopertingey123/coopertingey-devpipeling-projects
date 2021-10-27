# bin1 = input('Enter a binary number: ')
# bin2 = input('Enter a second binary number: ')
def bin_bin(num1, num2):
    if len(num2) > len(num1):
      greater_num = num2
      lesser_num = num1
    else:
      greater_num = num1
      lesser_num = num2
    lesser_num = lesser_num.zfill(len(greater_num))
    counter = -1
    string1 = []

    for char in greater_num and lesser_num:
        num_to_compare = greater_num[counter]
        num_to_compare2 = lesser_num[counter]
        index_of_str1 = num_to_compare + num_to_compare2
        string1.append(index_of_str1)
        counter -= 1
    return string1    
def bin_add(num1, num2):
    bin_add_list = ''
    bincompare = bin_bin(num1, num2)
    carry = 0
    for pair in bincompare:
        if carry == 0:
            if pair == '11':
                bin_add_list += '0'
                carry = 1
            elif pair == '00':
                bin_add_list += '0'
                carry = 0
            else:
                bin_add_list += '1'
                carry = 0
        else:  
            if pair == '11':
                bin_add_list += '1'
                carry = 1
            elif pair == '00':
                bin_add_list += '1'
                carry = 0
            else:
                bin_add_list += '0'
                carry = 1
    if carry > 0:
        bin_add_list += '1'
    # print(bin_add_list[::-1])
    return bin_add_list[::-1]



# A	B	 A x B
# 0	0	  0
# 0	1	  0
# 1	0	  0
# 1	1	  1

str1 = '111' #239 #'00111001' #57
str2 = '1111'#10023 #'00001111' #15   #855 #244,497


def bin_multiply(str1, str2):
  final = ''
  for i, char in enumerate(reversed(str2)):
    if char == '1':
      adding = str1 + ('0' * i)
      final = bin_add(final, adding)
  return print(final)

# bin_multiply('100', '100')

def bin_subtract(str1, str2):
  output = ''
  borrow = 0
  str1 = str1[::-1]
  str2 = str2[::-1]

  for i in range(str1):
    num1 = str1[i]
    num2 = str2[i]

    if num1 == num2:
      output += '0'
    
    if borrow == 1 and num1 == '1':
      num1 = '0'
  return


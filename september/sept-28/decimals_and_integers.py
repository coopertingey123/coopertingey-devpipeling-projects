def bin_to_dec(bin_num):
  total = 0
  range_of_nums = [128, 64, 32, 16, 8, 4, 2, 1]
  counter = 0
  for num in bin_num:
    if num == '1':
      total = total + range_of_nums[counter]
      counter += 1
    else:
      counter += 1
  print(total)

bin_to_dec('11111000')

dec_num = int(input('Enter in an integer: '))
my_string = ""
def dec_to_bin(dec_num):
  global my_string
  if dec_num >= 1:
      dec_to_bin(dec_num // 2)
  my_string += str(dec_num % 2 )


dec_to_bin (dec_num)

print(my_string)
# Start by making an empty list. Use a loop to add twelve random integers between 50 and 80, 
# inclusive, to the list. Sort the list in descending order from highest to lowest. Use a loop
#  to print the sorted list elements on one line separated by single spaces. Determine if 66 is in
#   the list and generate some appropriate output.
#  2.  Print the largest element in the list and the smallest element in the list. Slice
#   out the five elements with indexes 4 through 8 and assign to a variable. Print the  slice. Print
#    the total of all five elements in this slice. Use a while loop to display all elements in
#     the slice on one line separated by tabs. (edited) 

import random

list_nums = []
random_nums_list = []

for num in range(50, 81):
    list_nums.append(num)

i = 1
while i<12:
    random_num = random.randint(0, len(list_nums) -i)
    print(random_num)
    a = 3
    num1 = list_nums.pop(random_num)
    random_nums_list.append(num1)
    i+=1

print("random numbers list: ", random_nums_list)

new = sorted(random_nums_list)[::-1]

print("sorted list: ", new)

if 66 in new:
    print("66 is in the list")

print("max: ", max(new))
print("min: ", min(new))

sliced_nums = new[4:9]
print('sliced numbers list: ', sliced_nums)

total = 0
for num in sliced_nums:
    total += num

print('total of sliced numbers: ', total)

i = len(sliced_nums)
string_final = ''
while i > 0:
    for num in sliced_nums:
        string_final = string_final + str(num) + "   "
        i-=1
print('final string: ', string_final)
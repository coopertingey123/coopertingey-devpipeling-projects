# Write a Python program to test whether a number is within 100 of 1000 or 2000

def test(num):
    if num >= 1900 and num <= 2100:
        return True
    elif num >=900 and num <= 1100:
        return True
    else:
        return False


# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum

def three_nums(a, b, c):
    if a == b == c:
        return (a + b + c) * 3
    else:
        return a + b + c

# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user

def oddeven(num):
    if num % 2 == 0:
        return print("even")
    else:
        return print("odd")

# Write a Python program to count the number 4 in a given list

def count4(list1):
    counter=0
    for num in list1:
        if num == 4:
            counter += 1
        else:
            continue
    return print(f'4 appears {counter} times in the list')

# Write a Python program to test whether a passed letter is a vowel or not

def vowel(letter):
    if letter in ['a', 'e', 'i', 'o', 'u']:
        return print('Letter is a vowel')
    else:
        return print('Letter is a consonant')

# Write a Python program to concatenate all elements in a list into a string and return it.

def conc(list1):
    str1 = ''
    for st in list1:
        str1 = str1 + st
    return print(str1)

# Write a Python program to display your details like name, age, address in three different lines.

def display(name, age, address):
    print(f'My name is {name} \n')
    print(f'My age is {age} \n')
    print(f'My address is {address} \n')

# Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
def even(list1):
    list2 = []
    for num in list1:
        if num % 2 == 0:
            if num < 237:  
                list2.append(num)
    return print(list2)

even(numbers)


# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2

# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

def compare_lists(list1, list2):
    colors = []
    for color in list1:
        if color in list2:
            continue
        else:
            colors.append(color)


# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

# Write a Python program to add two objects if both objects are an integer type

# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3

# Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user

# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# Note: Do not use built-in functions.

#  Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number

# Write a Python program to convert an integer to binary keep leading zeros.
# Sample data : x=12
# Expected output : 00001100
# Write a Python program to write a Python list of lists to a csv file. After writing the CSV file read the CSV file and display the content.

# Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content

# Write a for loop so that every item in the list is printed.
# your_list=[“koala”, “cat”, “fox”, “panda”, “chipmunk”, “sloth”, “penguin”, “dolphin”]

# Write a for loop which print “Hello!, ” plus each name in the list. i.e.: “Hello!, Sam”
# your_list=[“Sam”, “Lisa”, “Micha”, “Dave”, “Wyatt”, “Emma”, “Sage”]
# Type a code inside the for loop so that counter variable named c is increased by one each time loop iterates.
# str=“Civilization”
# c=0
# for i in str:
# #Type your answer here.   
#   print(c)
# Add an if statement and a continue statement to the loop so that it skips when iterator equals “sun”.
# weather=[“sleet”, “snow”, “hail”, “rain”, “sun”, “clouds”]
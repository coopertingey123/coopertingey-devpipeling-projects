# STRINGS

# 1. replace the character H with the letter J
# txt = "Hello World"
# txt = txt.___( ____, ___)
def replace_h(str1):
    print(str1.replace("H", "J"))

# replace_h("Hello world")


# 2. covert the text to lowercase
# txt = "HELLO WORLD"
# txt = ____________
def lowercase(txt):
    print(txt.lower())
lowercase("HELLO WORLD")


# ***Numbers***


# 8. create a lambda function that takes in one parameter ( a ) and returns it
# x = ________ _ _ _ 
# x = lambda a : a 

# 9. Write a function that will take any given sequence of numbers and determines whether all the numbers are differe from each other.
def different(list_num):
    for num in list_num:
        counter = list_num.count(num)
        if counter > 1:
            return print('NOOOO')
        else:
            continue
    return print("there are no repeats")
# different([9,8,7,6,5,4,5])        


# 10. using the random library which we have used a lot, Write a python program to create all possible strings by using 'a' 'e' 'i' 'o' 'u' 
# ( examples of output aeiou, eioua, uoiea etc....)
import random

def vowels():
    vowels = 'aeiou'
    new_list = []
    result = list(vowels)
    
    while result not in new_list:
        result = random.shuffle(result)
        new_list.append(result)
    return print(new_list)
vowels()
#still needs work



# 11. Write a python program to remove and print every 3rd number from a given list of numbers and will repeat until the list is empty ( 11, 12, 13, 14, 15, 16, 17, 18, 19, 20   should print 11, 14, 17, 20 and then stop..)

# 12 write a python function to concatenate all elements in a list into a string and return it 

# 13. using the datetime library write a program to calculate the number of days between two dates.

# 14. write a program that displays the first and last elements from this list
# cars = ["Ford", "Chevy", "BMW", "Bentley", "Honda"]

# 16. Write a python program that will take in a first and last name and print them in reverse order

# 17. Write a python program to read each row from the csv file with this data inside
# ( you will need to create the csv file and then copy and past this into it.)
# department_id,department_name,manager_id,location_id
# 10,Administration,200,1700
# 20,Marketing,201,1800
# 30,Purchasing,114,1700
# 40,Human Resources,203,2400
# 50,Shipping,121,1500
# 60,IT,103,1400
# 70,Public Relations,204,2700
# 80,Sales,145,2500
# 90,Executive,100,1700
# 100,Finance,108,1700
# 110,Accounting,205,1700
# 120,Treasury,,1700
# 130,Corporate Tax,,1700
# 140,Control And Credit,,1700   


# 18. Using the same csv file from before write a program that will read from the file as a dictionary.
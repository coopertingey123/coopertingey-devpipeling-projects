# my_string = "Coding in Python is amazing"

# print(my_string[10:16])

# my_string = "The quick brown fox jumps over the lazy dog"

# print(my_string[10:25])


# my_tuple = (1, 5, 89, 234, 289, 445, 578, 623, 777, 898, 900)

# print(my_tuple[3:9])

# my_list = []
# for num in range(28):
#     my_list.append(num)

# print(my_list[4:21:2])


my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

def slice_function(list1, start1, end1):
    new_list = []
    for i, char in enumerate(list1, start=start1):
        print(f'i: {i}')
        print(f'char: {char}')
        if i < end1:
            new_list.append(list1[i])
        else:
            continue
    
    return new_list

print(slice_function(my_list, 2, 8))

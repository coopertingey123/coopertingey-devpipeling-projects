# input1 = int(input("What is your number?"))
# full_name = lambda first : first + input1
# print(full_name(5))
# -------------------------------------
# tuples = [('civic', 98, 'lamest car'), ('f150', 87, 'the awesomest of awesome car'), ('mustang', 21, 'super cool car')]
# tuples.sort(key = lambda item: item[2])
# print(tuples)
# -------------------------------------
# cars = [{
#     'make': 'ford',
#     'model': 'mustang',
#     'year': 1998
# }, {
#     'make': 'tesla',
#     'model': 'model 3',
#     'year': 2018
# }, {
#     'make': 'honda',
#     'model': 'civic',
#     'year': 2014
# }, {
#     'make': 'corvette',
#     'model': 'stingray',
#     'year': 2021
# }]

# sort_key = input("How would you like to sort the cars? (make, model, year) \n Answer: ").lower()

# def sort_list_cars(key_to_sort):
#     cars.sort(key = lambda car: car[key_to_sort])
#     print(cars)

# sort_list_cars(sort_key)
# ---------------------------------

import random

lottery_dict = {
    'green': 3,
    'red': 7,
    'pink': 2
}
run = True

new_list=[]
for color in lottery_dict:
    for num in range(lottery_dict[color]):
        new_list.append(color)

while run:
    user_input = input("Would you like to pick? (y/n)")
    if new_list == []:
        run = False
    elif user_input == 'y':
        print(new_list)
        print()
        random_num = random.randint(0, (len(new_list) -1))
        selected_color = new_list[random_num]
        print(f'You selected {selected_color}')
        print()
        new_list.remove(selected_color)
        continue
    elif user_input == 'n':
        run = False
    else:
        run = False
print('\nThank you for playing!')

# ---------------------------------------------------
    

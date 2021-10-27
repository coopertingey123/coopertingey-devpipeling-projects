cars = [ 'mustang', 'corvette', 'civic', 'f150', 'tesla', 'kicks', 'crv' ]

with open("new_file.txt", "w") as cars_list:
    for car in cars:
        cars_list.write('%s\n'%car)

with open("new_file.txt", "rt") as cars_list:
    print(cars_list.read())

print()

list1 = []
with open("new_file.txt", "r+") as file:
    lines = file.readlines()
    for line in lines:
        item = line[:-1]
        list1.append(item)
    print(list1)
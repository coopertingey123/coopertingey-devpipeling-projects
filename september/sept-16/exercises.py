
# Number 1

with open("fruits.txt", "wt") as fruits:

    list_of_fruit= ["orange", "banana", "apple", "grape"]

    for fruit in list_of_fruit:
        fruits.write(f"{fruit}\n")

with open("fruits.txt", "r") as fruits:
    print(fruits.read())

with open("fruits.txt", "at") as fruits:
    fruits.write("pineapple\n")

with open("fruits.txt", "r") as fruits:
    print(fruits.read())


# Number 2


with open("cars.txt", "wt") as cars:

    list_of_cars= ["toyota", "honda", "lambo", "corvette"]

    for car in list_of_cars:
        cars.write(f"{car}\n")

with open("cars.txt", "r") as cars:
    print(cars.read())

with open("cars.txt", "wt") as shoes:

    list_of_shoes= ["reebok", "nike", "adidas", "vans"]

    for shoe in list_of_shoes:
        shoes.write(f"{shoe}\n")

with open("cars.txt", "r") as shoes:
    print(shoes.read())


# Number 3

with open("numbers.txt", "wt") as numbers:

    for num in range(11):
        numbers.write(f"{num}\n")

with open("numbers.txt", "r") as numbers:
    print(numbers.read())
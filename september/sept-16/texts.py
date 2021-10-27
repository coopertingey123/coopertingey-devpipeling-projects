
with open("example.txt", "r") as my_file:

    for line in my_file:
        print(line)



new_file = open("example.txt", "r")

print(new_file.read())

new_file.close()
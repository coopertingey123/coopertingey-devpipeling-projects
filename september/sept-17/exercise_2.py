# function that finds the longest word in a text file

def find_biggest_word(file):
    with open(file, "r") as text:
        result = []
        text1 = text.read()
        new_lines = text1.split()
        max_chars = new_lines[0]
        for line in new_lines:            
            if len(line) >= len(max_chars):
                max_chars = line
                result.append(line)
        return print(result)

find_biggest_word("example1.txt")
find_biggest_word("testing_one.txt")
find_biggest_word("text_two.txt")

# Write a python dictionary and return that dictionary in another file
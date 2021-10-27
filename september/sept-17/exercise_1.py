def line_counter(file):
    with open(file, "r") as text:
        counter = 0
        content = text.read()
        for line in content:
            if line == "\n":
                counter += 1
        print(f"There are {counter} lines in the file {file}.")
        return counter

var1 = line_counter("text_two.txt")
var2 = line_counter("testing_one.txt")

print(var1, var2)

def add_counters(count1, count2):
    total = count1 + count2
    return f"The total number of lines for the two text files is {total} lines."

print(add_counters(var1, var2))




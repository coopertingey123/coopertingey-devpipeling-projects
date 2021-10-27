with open("quotes4.txt", "r") as quotes:
    for line in quotes:
        print(line)

with open("quotes4.txt", "r") as quotes2:
    lines = quotes2.readlines()
    count = 0
    for line in lines:
        count += 1
        print(f"{line.strip()}\n")

with open("quotes4.txt", "r") as quotes3:
    while True:

        count += 1
        line = quotes3.readline()

        if not line:
            break

        print(f"{line.strip()}\n")


import os

file_finder = os.listdir()

for filepath in file_finder:
    if os.path.isdir(filepath):
        print('/' + filepath)
    else:
        print(filepath)


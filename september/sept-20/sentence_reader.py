# with open("txt1.txt", "r") as sentences:
#     txt = sentences.read()
#     new_txt = txt.split(". ")
#     # print(new_txt)
#     for sentence in new_txt:
#         if "." not in sentence:
#             print(sentence + ".")
#         else:
#             print(sentence)


with open('raw_data.txt', 'r') as superheros:
    txt = superheros.read()

with open('raw_data.txt', 'w') as superheros2:
    split_txt = txt.split('|')
    join_txt = ",".join(split_txt)
    superheros2.write(join_txt)

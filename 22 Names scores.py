import string

alphabet_score = dict(zip(string.ascii_uppercase, range(1, 27)))

names_file = open("22_names.txt", "rt")
names = names_file.read()
names_file.close()
names = sorted(names.replace('"', "").split(","))

total_name_score = 0

for order, name in enumerate(names):
    name_score = 0
    for letter in name:
        name_score += alphabet_score[letter]
    name_score *= order + 1
    total_name_score += name_score
print(total_name_score)

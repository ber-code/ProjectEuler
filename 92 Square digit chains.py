from time import perf_counter

tic = perf_counter()


def chain(num):
    chain_num, new_ends = int(num), [num]
    while chain_num not in eightynines:
        if chain_num in ones:
            for end in new_ends:
                ones.add(num)
                return False
        chain_num = sum([int(i) ** 2 for i in str(chain_num)])
        new_ends.append(chain_num)
    for end in new_ends:
        eightynines.add(end)
    return True


eightynines = {89}
ones = {1}
count = 0
for num in range(1, 10000000):
    add = chain(num)
    if add:
        count += 1

print(count)
toc = perf_counter()
print("Dis code take {time} seconds".format(time=toc - tic))

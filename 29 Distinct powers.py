bounds = range(2, 101)
distinct = set()
for a in bounds:
    for b in bounds:
        distinct.add(a ** b)
print(len(distinct))

def sum_multiples_below(cap, factors):
    multiples = set()
    for i in factors:
        step = i
        while step < cap:
            multiples.add(step)
            step += i
    return sum(multiples)


print(sum_multiples_below(1000, [3, 5]))

import itertools

four_digit_primes_set = set()
primes = [2]


def prime_generator(num, target):
    for prime in primes:
        if prime > num ** 0.5:
            break
        if num % prime == 0:
            return
    primes.append(num)
    if len(str(num)) == target:
        four_digit_primes_set.add(num)


for num in range(3, 10000):
    prime_generator(num, 4)

visited = set()
for prime in four_digit_primes_set:
    ret = []
    for perm in itertools.permutations(str(prime), 4):
        check = int("".join(perm))
        if check in four_digit_primes_set:
            ret.append(check)
    ret = sorted(list(set(ret)))
    if len(ret) >= 3:
        for low in range(len(ret) - 2):
            if ret[low] in visited:
                break
            for mid in range(low + 1, len(ret) - 1):
                difference = ret[mid] - ret[low]
                for end in range(mid + 1, len(ret)):
                    if ret[mid] + difference == ret[end]:
                        visited.add(ret[low])
                        visited.add(ret[mid])
                        visited.add(ret[end])
                        print("".join(str(i) for i in [ret[low], ret[mid], ret[end]]))
                        break

import time

print("Working...")
tic = time.perf_counter()

primes = []
f = open("60 primes.txt", "r")
for count, line in enumerate(f):
    primes.append(int(line.strip(" \n\t")))
f.close()
primes_set = set(primes)


def concats_are_prime(num_list, new_num):
    for num in num_list:
        if not (
            int(str(num) + str(new_num)) in primes_set
            and int(str(new_num) + str(num)) in primes_set
        ):
            return False
    return True


def combo_finder(target_length, max_prime_length):
    ret = float("inf")
    stop = False

    def recurser(combo, pointer, remaining_length):
        nonlocal ret, stop
        if len(combo) == target_length:
            ret = min(ret, sum(combo))
            print("New combo is:", combo, "sum is:", sum(combo))
            stop = True
            return
        while len(str(primes[pointer])) <= remaining_length:
            if not combo and len(str(primes[pointer])) > remaining_length // 2:
                return
            if concats_are_prime(combo, primes[pointer]):
                new_combo = list(combo)
                new_combo.append(primes[pointer])
                recurser(
                    new_combo,
                    pointer + 1,
                    min(remaining_length, max_prime_length - len(str(new_combo[-1]))),
                )
            if stop:
                return
            pointer += 1

    recurser([], 0, max_prime_length)


combo_finder(5, 8)

toc = time.perf_counter()
print("Crunched in {time} seconds".format(time=toc - tic))

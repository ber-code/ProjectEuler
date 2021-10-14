test, primes = 3, []
while len(str(test)) <= 8:
    test_is_prime = True
    for prime in primes:
        if prime > int(test ** 0.5):
            break
        if test % prime == 0:
            test += 2
            test_is_prime = False
            break
    if test_is_prime:
        primes.append(test)
        test += 2
f = open("primes.txt", "w")
for prime in primes:
    f.write(str(prime) + "\n")
f.close()

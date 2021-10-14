def list_and_set_of_primes_below(n):
    primes_list = [2]
    check = 3
    while check < n:
        check_is_prime = True
        for prime in primes_list:
            if prime > check ** 0.5:
                break
            if check % prime == 0:
                check_is_prime = False
                break
        if check_is_prime:
            primes_list.append(check)
        check += 2
    return primes_list, set(primes_list)


# initialize
cap = 1000000
primes_list, primes_set = list_and_set_of_primes_below(cap)
idx_start = idx_end = working_sum = answer = 0
while working_sum < cap:
    working_sum += primes_list[idx_end]
    if working_sum in primes_set:
        answer, start_ret, end_ret = working_sum, int(idx_start), int(idx_end)
    idx_end += 1
working_sum, idx_start, idx_end = int(answer), int(start_ret), int(end_ret)

# algorithm
while working_sum < cap:
    working_sum -= primes_list[idx_start]
    idx_start += 1
    idx_end += 1
    working_sum += primes_list[idx_end]
    temp_end, temp_sum = int(idx_end), int(working_sum)
    while temp_sum < cap:
        if temp_sum in primes_set and (temp_end - idx_start) > (end_ret - start_ret):
            answer, start_ret, end_ret = temp_sum, idx_start, temp_end
        temp_end += 1
        temp_sum += primes_list[temp_end]
print(answer)

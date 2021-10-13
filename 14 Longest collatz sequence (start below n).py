def longest_collatz_starting_below(n):
    answer = 1
    max_length = 1
    for start in range(2, n):
        start_trial = int(start)
        trial_length = 0
        while start > 1:
            trial_length += 1
            if start % 2 == 0:
                start //= 2
            else:
                start = 3 * start + 1
        if trial_length > max_length:
            max_length = trial_length
            answer = start_trial
    return answer


print(longest_collatz_starting_below(1000000))

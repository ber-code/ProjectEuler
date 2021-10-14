memo = {}
check = 11
while True:
    cubed = check ** 3
    new_memo = "".join(sorted(str(cubed)))
    if new_memo not in memo:
        memo[new_memo] = [cubed, 1]
    else:
        memo[new_memo][1] += 1
        if memo[new_memo][1] == 5:
            print(memo[new_memo])
            break
    check += 1

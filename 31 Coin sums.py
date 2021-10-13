def ways_to_make_change(total, coins):
    if not coins:
        if total:
            return 0
        return 1
    ways = [1] + [0] * total
    for coin in coins:
        for j in range(coin, total + 1):
            ways[j] += ways[j - coin]
    return ways[-1]


print(ways_to_make_change(200, [1, 2, 5, 10, 20, 50, 100, 200]))

"""
Insight:
this is the same as # of ways to make a sum given coins, but you have every coin value
"""


def change(amount, coins):
    if not coins:
        if amount:
            return 0
        return 1
    ways = [1] + [0] * amount
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[-1]


print(change(100, range(1, 100)))

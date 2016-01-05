import sys


def minimal_coins_iterative(coins, amount):

    # The value of each coin can be formed by one coinÒ
    amount_of_coins = [sys.maxsize]*(amount + 1)
    amount_of_coins[0] = 0
    for i in coins:
        amount_of_coins[i] = 1

    for i in range(amount+1):
        for j in coins:
            if j < i and amount_of_coins[i-j] + 1 < amount_of_coins[i]:
                amount_of_coins[i] = amount_of_coins[i-j] + 1
    return amount_of_coins[amount]


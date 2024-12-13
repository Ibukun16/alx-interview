#!/usr/bin/python3
"""A module that handles prime game
"""


def isWinner(x, nums):
    """Function that determines the winer of a
    prime game session at `x` round.
    """
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0

    # generates primes with a limit of the maximum number in nums
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for c in range(2, int(max_num**0.5) + 1):
        if primes[c]:
            for r in range(c**2, max_num + 1, c):
                primes[r] = False

    # remove prime and its multiple from max_num in each round
    for num in nums:
        count_primes = sum(primes[2:num+1])
        ben_wins += count_primes % 2 == 0
        maria_wins += count_primes % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Ben' if ben_wins > maria_wins else 'Maria'

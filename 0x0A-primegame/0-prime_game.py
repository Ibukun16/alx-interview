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
    primes = [True for _ in range(1, max_num + 1)]
    primes[0] = False
    for c, is_prime in enumerate(primes, 1):
        if c == 1 or not is_prime:
            continue
        for r in range (c + c, max_num + 1, c):
            primes[r - 1] = False

    # remove prime and its multiple from max_num in each round
    for _, max_num in zip(range(x), nums):
        count_primes = len(list(filter(lambda x: x, primes[0: max_num])))
        ben_wins += count_primes % 2 == 0
        maria_wins += count_primes % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Ben' if ben_wins > maria_wins else 'Maria'
    

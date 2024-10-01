#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
    x (int): The number of rounds.
    nums (list): An array of n for each round.

    Returns:
    str: Name of the player that won the most rounds.
         If the winner cannot be determined, returns None.
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    def sieve_of_eratosthenes(n):
        """
        Generates primes up to n using the Sieve of Eratosthenes algorithm.

        Args:
        n (int): Upper limit for generating primes.

        Returns:
        list: A list of boolean values where True indicates a prime number.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return primes

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        prime_count = sum(primes)

        # If the number of primes is odd, Maria wins, otherwise Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("This module is not meant to be executed directly.")

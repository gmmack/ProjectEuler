"""Calculates the 10,001st prime number and prints it.
   Project Euler #7"""

import math
def print_list (lst):
    for i in lst:
        print i

def is_prime (num):
    sqrt = int(math.sqrt(num)+1)
    for i in range(2,sqrt):
        if num % i == 0:
            return False
    return True

def get_10_001(primes):
    count = 0
    for prime in primes:
        count += 1
        if count == 10001:
            return prime

def generate_primes ():
    primes = []
    for i in range(2,1000000):
        if is_prime(i):
            primes.append(i)
    return primes

primes = generate_primes()
"""print_list(primes)"""
solution = get_10_001(primes)
print solution

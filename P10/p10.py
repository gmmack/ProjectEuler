"""Sums all primes below 2 million and prints result"""

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

def sum_primes(primes):
    summ = 0
    for prime in primes:
        if prime > 2000000:
            break
        else:
            summ += prime
    return summ
        

def generate_primes ():
    primes = []
    for i in range(2,2000001):
        if is_prime(i):
            primes.append(i)
    return primes

primes = generate_primes()
"""print_list(primes)"""
solution = sum_primes(primes)
print solution

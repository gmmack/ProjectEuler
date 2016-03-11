"""Calculates the difference between the sum of the squares
   of the first one hundred natural numbers and the square
   of the sum and prints the result. Project Euler #6"""

def sum_of_squares ():
    summ = 0
    for i in range(1,101):
        summ += i**2
    return summ

def square_of_sums ():
    summ = 0
    for i in range(1,101):
        summ += i
    return summ**2

print square_of_sums()-sum_of_squares()

# Smallest multiple

import math

# Solution 1 (only possible with Python 3.9+)
print(math.lcm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20))


def first_n_integers(n):                    # Solution 2
    return [i for i in range(1, n + 1)]


def find_lcm(lst):
    lcm = 1
    for i in lst:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm


print(find_lcm(first_n_integers(10)))       # prints 2520
print(find_lcm(first_n_integers(20)))       # prints 232792560

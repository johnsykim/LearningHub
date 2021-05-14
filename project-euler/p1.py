# Multiples of 3 and 5

lst = [n for n in range(1000) if n % 3 == 0 or n % 5 == 0]
print(sum(lst))

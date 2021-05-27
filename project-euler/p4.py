# Largest palindrome product

def check_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


def solution_1():
    prods = []
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            prod = i * j
            prods.append(prod)
    prods = [n for n in prods if check_palindrome(n)]
    return max(prods)


def solution_2():
    largestPalindrome = 0
    a = 999
    while a >= 100:
        b = 999
        while b >= a:
            if a*b <= largestPalindrome:
                break  # Since a*b is always going to be too small
            if check_palindrome(a*b):
                largestPalindrome = a*b
            b -= 1
        a -= 1
    return largestPalindrome


if __name__ == '__main__':
    print(solution_1())     # prints 906609
    print(solution_2())     # prints 906609

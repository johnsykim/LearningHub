import sys


def bela():
    N, B = sys.stdin.readline().split()
    data = [sys.stdin.readline().strip() for i in range(4 * int(N))]

    value_table = {'A': (11, 11),
                   'K': (4, 4),
                   'Q': (3, 3),
                   'J': (20, 2),
                   'T': (10, 10),
                   '9': (14, 0),
                   '8': (0, 0),
                   '7': (0, 0)}

    sum = 0
    for card in data:
        number, suit = card[0], card[1]

        # Retrieve score value depending on whether the suit is dominant
        if suit == B:
            sum += value_table.get(number)[0]
        else:
            sum += value_table.get(number)[1]

    return sum


print(bela())

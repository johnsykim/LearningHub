# Sum square difference

class custom_calc:
    def __init__(self, n):
        self.n = n

    def sum_of_squares(self):
        res = 0
        for i in range(1, self.n + 1):
            res += i ** 2
        return res

    def square_of_sum(self):
        return sum([n for n in range(1, self.n + 1)]) ** 2


if __name__ == '__main__':
    my_calc = custom_calc(100)
    print(my_calc.sum_of_squares())
    print(my_calc.square_of_sum())
    print(my_calc.square_of_sum() - my_calc.sum_of_squares())

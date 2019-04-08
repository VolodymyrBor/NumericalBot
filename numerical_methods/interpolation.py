import math
import sys
from sympy import Symbol, pprint


class Lagrange:
    def __init__(self, equation, begin, end, h,  x_value):

        x_coordinates = []
        y_coordinates = []
        func = Symbol('x')
        x = Symbol('x')
        func = eval(equation)
        while begin <= end :
            x_coordinates.append(begin)
            y_coordinates.append(func.subs(x, begin))
            begin += h

        lgrange_polynomial = 0
        for i in range(len(x_coordinates)):
            numerator = y_coordinates[i]
            denominator = 1
            for x_item in x_coordinates:
                if x_coordinates[i] != x_item:
                    numerator *= (x - x_item)
                    denominator *= (x_coordinates[i] - x_item)
            lgrange_polynomial += numerator / denominator

        file = open('data.txt', 'w')
        sys.stdout = file
        print(lgrange_polynomial)
        lgrange_polynomial = lgrange_polynomial.expand()
        print('\n')
        print(lgrange_polynomial)
        print('\n')
        print(lgrange_polynomial.evalf())
        print('\n')
        print('f({}) = {}'.format(x_value, lgrange_polynomial.subs(x, x_value)))
        file.close()




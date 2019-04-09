import math
import sys
from sympy import Symbol, pprint, poly


class Lagrange:

    def __init__(self, equation, begin, end, h,  x_value):

        x_coordinates = []
        y_coordinates = []
        x = Symbol('x')
        func = eval(equation)
        while begin <= end:
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

        file = open('data.txt', 'w', encoding='utf-8')
        terminal = sys.stdout
        sys.stdout = file

        pprint(lgrange_polynomial)
        lgrange_polynomial = lgrange_polynomial.expand()

        print('\n')
        pprint(lgrange_polynomial)
        print('\n')
        pprint(lgrange_polynomial.together())
        print('\n')
        pprint(lgrange_polynomial.evalf())
        print('\n')

        for i in range(len(x_coordinates)):
            print('L({}) = {}\tf({}) = {}\n'.format(*map(float, [x_coordinates[i], self.gorner(lgrange_polynomial,
                                                    x_coordinates[i]), x_coordinates[i], y_coordinates[i]])))

        print('L({}) = {}\tf({}) = {}\n'.format(x_value, self.gorner(lgrange_polynomial, x_value),

                                                x_value, func.subs(x, x_value)))
        file.close()
        sys.stdout = terminal

    def gorner(self, f, x_value):
        x = Symbol('x')
        coof = poly(f).coeffs()
        ans = 0
        for k in coof:
            ans = k + ans*x_value
        return ans





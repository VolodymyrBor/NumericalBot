import math
import sys
from sympy import Symbol, pprint


class Lagrange:
    def __init__(self, x_coordinates: list, y_coordinates: list, x_value):
        x = Symbol('x')
        lgrange_polynomial = 0
        file = open('numerical_methods\data.txt', 'w')
        for i in range(len(x_coordinates)):
            numerator = y_coordinates[i]
            denominator = 1
            for x_item in x_coordinates:
                if x_coordinates[i] != x_item:
                    numerator *= (x - x_item)
                    denominator *= (x_coordinates[i] - x_item)
            lgrange_polynomial += numerator / denominator
        file.write(str(lgrange_polynomial))
        lgrange_polynomial = lgrange_polynomial.expand()
        file.write('\n\n{}\n'.format(lgrange_polynomial))
        file.write('\n{}\n\n'.format(lgrange_polynomial.evalf()))
        file.write('f({}) = {}'.format(x_value, lgrange_polynomial.subs(x, x_value)))
        file.close()




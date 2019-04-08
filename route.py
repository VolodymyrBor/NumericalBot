from errors import ErrorData, ErrorMethod
from numerical_methods.numerical import Bisection, EulerMethod, RungeKutta
from numerical_methods.interpolation import Lagrange
import math


class Route:
    def __init__(self, kwargs):
        if kwargs is not None:
            if kwargs['method'] == 'bisection':
                Bisection(n=kwargs['n'], m=kwargs['m'], equation=kwargs['equation'])
            if kwargs['method'] == 'euler':
                EulerMethod(equation=kwargs['equation'], x=kwargs['x'], y=kwargs['y'], h=kwargs['h'], begin=kwargs['begin'], end=kwargs['end'])
            if kwargs['method'] == 'rungekutta':
                RungeKutta(equation=kwargs['equation'], x=kwargs['x'], y=kwargs['y'], h=kwargs['h'], begin=kwargs['begin'], end=kwargs['end'])
            if kwargs['method'] == 'lagrange':
                Lagrange(equation=kwargs['equation'], begin=kwargs['begin'], end=kwargs['end'], h=kwargs['h'], x_value=kwargs['x_value'])


class ChooseMethods:
    def __init__(self, message):
        self.list_methods = ['bisection', 'euler', 'rungekutta', 'lagrange']
        self.data = [*message.split()]
        self.kwargs = None
        if self.data[0] in self.list_methods:
            ChooseMethods.data_processor(self)
        else:
            ErrorMethod()

    def check_equation(self, x=0):
        try:
            eval(self.kwargs['equation'])
        except Exception:
            ErrorData()
        else:
            return self.kwargs

    def data_processor(self):
        if self.data[0] == 'bisection':
            try:
                self.kwargs = {
                    'method': self.data[0],
                    'n': float(self.data[1]),
                    'm': float(self.data[2]),
                    'equation': self.data[3]
                }
            except Exception:
                ErrorData()
            self.kwargs = self.check_equation()

        if self.data[0] in ['euler', 'rungekutta']:
            try:
                self.kwargs = {
                    'method': self.data[0],
                    'equation': self.data[1],
                    'x': float(self.data[2]),
                    'y': float(self.data[3]),
                    'h': float(self.data[4]),
                    'begin': float(self.data[5]),
                    'end': float(self.data[6])
                }
            except Exception:
                ErrorData()
            self.kwargs = self.check_equation()

        if self.data[0] == 'lagrange':
            try:
                self.kwargs = {
                    'method': self.data[0],
                    'equation': self.data[1],
                    'begin': float(self.data[2]),
                    'end': float(self.data[3]),
                    'h': float(self.data[4]),
                    'x_value': float(self.data[5])
                }
            except Exception:
                ErrorData()
            self.kwargs = self.check_equation()

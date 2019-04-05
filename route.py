from errors import ErrorData, ErrorMethod
from numerical import Bisection, EulerMethod, RungeKutta


class Route:
    def __init__(self, kwargs):
        if kwargs is not None:
            if kwargs['method'] == 'bisection':
                Bisection(n=kwargs['n'], m=kwargs['m'], equation=kwargs['equation'])
            if kwargs['method'] == 'euler':
                EulerMethod(equation=kwargs['equation'], x=kwargs['x'], y=kwargs['y'], h=kwargs['h'], begin=kwargs['begin'], end=kwargs['end'])
            if kwargs['method'] == 'rungekutta':
                RungeKutta(equation=kwargs['equation'], x=kwargs['x'], y=kwargs['y'], h=kwargs['h'], begin=kwargs['begin'], end=kwargs['end'])


class ChooseMethods:
    def __init__(self, message):
        self.list_methods = ['bisection', 'euler', 'rungekutta']
        self.data = [*message.split()]
        self.kwargs = None
        if self.data[0] in self.list_methods:
            ChooseMethods.data_processor(self)
        else:
            ErrorMethod()

    def data_processor(self):
        if self.data[0] == 'bisection':
            try:
                self.kwargs = {
                    'method': self.data[0],
                    'n': float(self.data[1]),
                    'm': float(self.data[2]),
                    'equation': self.data[3]
                }
            except ValueError:
                self.kwargs = None
                ErrorData()

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
            except ValueError:
                self.kwargs = None
                ErrorData()

from errors import ErrorData, ErrorMethod
from numerical_methods.numerical import Bisection, EulerMethod, RungeKutta
from numerical_methods.interpolation import Lagrange


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
                Lagrange(x_coordinates=kwargs['x_coordinates'], y_coordinates=kwargs['y_coordinates'], x_value=kwargs['x_value'])


class ChooseMethods:
    def __init__(self, message):
        self.list_methods = ['bisection', 'euler', 'rungekutta', 'lagrange']
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
        if self.data[0] == 'lagrange':
            x_coordinates = []
            y_coordinates = []
            try:
                coordinates = self.data[1].split('|')
                x_value = self.data[2]
                for item in coordinates:
                    x, y = map(float, item.split(';'))
                    x_coordinates.append(x)
                    y_coordinates.append(y)
                self.kwargs = {
                    'method': self.data[0],
                    'x_coordinates': x_coordinates,
                    'y_coordinates': y_coordinates,
                    'x_value': float(x_value)
                }
            except ValueError:
                self.kwargs = None
                ErrorData()

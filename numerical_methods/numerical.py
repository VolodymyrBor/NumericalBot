import math


class Bisection:
    def __init__(self, n=None, m=None, equation=None):
        def is_null(x):
            if eval(equation) == 0:
                return True
            else:
                return False

        def calculation(x):
            return eval(equation)

        def division(a, b, itr=0, E =10**(-3)):
            itr += 1
            c = (a + b) / 2
            if is_null(c):
                return c
            if math.fabs(a - b) < E:
                x = (a + b) / 2
                count = 'x=' + str(x) + '  E=' + str(math.fabs(a - b)) + '     itr:' + str(itr) + '\n' + str(
                    eval(equation)) + ' ~ 0'
                return count
            if calculation(a) * calculation(c) < 0:
                return division(a, c, itr)
            elif calculation(c) * calculation(b) < 0:
                return division(c, b, itr)
        f = open('numerical_methods\data.txt', 'w')
        f.write(division(a=int(n), b=int(m)))
        f.close()


class EulerMethod:
    def __init__(self, equation, x, y, h, begin, end):

        def cal(x, y):
            return eval(equation)

        f = open('numerical_methods\data.txt', 'w')
        i = 0
        while i <= (end - begin) / h:
            derivative = cal(x, y)
            delta_y = h * derivative
            f.write("i= {}\tx= {}\ty= {}\ty'= {}\tDelta y= {} \n".format(i, x, y, derivative, delta_y))
            x += h
            y += delta_y
            i += 1

        f.close()


class RungeKutta:
    def __init__(self, equation, x, y, h, begin, end):
        E = 0.09

        def f(x, y):
            return eval(equation)

        def O_control(k1, k2, k3):
            ret = abs((k2 - k3) / (k1 - k2))
            return ret <= E

        i = 0
        x_mas = [x]
        y_mas = [y]
        pos = begin

        while (pos < end):
            x = x_mas[i]
            y = y_mas[i]
            k1 = h * f(x, y)
            k2 = h * f(x + h / 2, y + k1 / 2)
            k3 = h * f(x + h / 2, y + k2 / 2)
            k4 = h * f(x + h, y + k3)
            if (O_control(k1, k2, k3)):
                pos += h;
                dy = (k1 + 2 * k2 + 2 * k3 + k4) / 6
                i += 1
                x_mas.append(x + h)
                y_mas.append(y + dy)
            else:
                h /= 2

        file = open('numerical_methods\data.txt', 'w')
        for i in range(len(x_mas)):
            file.write('i={}\t|\tx={}\t|\ty={}\n'.format(i, x_mas[i], y_mas[i]))
        file.close()

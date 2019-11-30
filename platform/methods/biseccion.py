from math import *
from prettytable import PrettyTable


class Biseccion:
    def __init__(self, function, value_a, value_b, iterations, decimals):
        self.function = function
        self.value_a = value_a
        self.value_b = value_b
        self.iterations = iterations
        self.decimals = decimals

    # Functions
    @staticmethod
    def evaluate(fun, x):
        try:
            return eval(fun)
        except (ValueError, NameError) as ex:
            return ex

    def method(self):
        table = PrettyTable(['it', 'A', 'B', 'Fa', 'Fb', 'xi', 'Xi'])
        #
        print('')
        print('[METODO DE BISECCION]')
        print('Función = ', self.function)
        print('Valores de los puntos [A, B] respectivamente [', self.value_a, ', ', self.value_b, ']')
        print('Número de iteraciones a evaluar: ', self.iterations)
        print('Número de decimales que se tomaran en cuenta: ', self.decimals)
        print('')
        print('Solución:')
        #
        for it in range(self.iterations):
            Fa_tmp = self.evaluate(self.function, self.value_a)
            Fa = round(Fa_tmp, self.decimals)
            Fb_tmp = self.evaluate(self.function, self.value_b)
            Fb = round(Fb_tmp, self.decimals)
            xi_tmp = (self.value_a + self.value_b) / 2
            xi = round(xi_tmp, self.decimals)
            Fxi_temp = self.evaluate(self.function, xi)
            Fxi = round(Fxi_temp, self.decimals)
            table.add_row([it, self.value_a, self.value_b, Fa, Fb, xi, Fxi])
            if Fa > 0 and Fb > 0:
                break
            elif Fa < 0 and Fb < 0:
                break
            else:
                if Fxi >= 0 and Fa >= 0:
                    self.value_a = round(xi, self.decimals)
                    self.value_b = round(self.value_b, self.decimals)
                elif Fxi >= 0 and Fb >= 0:
                    self.value_a = round(self.value_a, self.decimals)
                    self.value_b = round(xi, self.decimals)
                elif Fxi < 0 and Fa < 0:
                    self.value_a = round(xi, self.decimals)
                    self.value_b = round(self.value_b, self.decimals)
                elif Fxi < 0 and Fb < 0:
                    self.value_a = round(self.value_a, self.decimals)
                    self.value_b = round(xi, self.decimals)
        print(table)


biseccion = Biseccion('2 * x + pow(x, 3) - 10', 1, 2, 5, 2)
biseccion.method()

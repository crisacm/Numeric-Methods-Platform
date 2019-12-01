from math import *
from prettytable import PrettyTable


class ReglaFalsa:
    def __init__(self, function, value_a, value_b, iterations, decimals):
        self.function = function
        self.value_a = value_a
        self.value_b = value_b
        self.iterations = iterations
        self.decimals = decimals

    @staticmethod
    def validate(fun, x):
        try:
            eval(fun)
            return True
        except (ValueError, NameError):
            return False

    @staticmethod
    def evaluate(fun, x):
        try:
            return eval(fun)
        except (ValueError, NameError) as ex:
            return ex

    def evaluate_xi(self, Fa, Fb):
        try:
            a = self.value_a
            b = self.value_b
            function = '(a * Fb - b * Fa) / (Fb - Fa)'
            return eval(function)
        except (ValueError, NameError) as ex:
            return ex

    def method(self):
        break_state = 0
        table = PrettyTable(['it', 'A', 'B', 'Fa', 'Fb', 'xi', 'Xi'])
        #
        print('')
        print('> SOLUCION:')
        print('Función = ', self.function)
        print('Valores de los puntos [A, B] respectivamente [', self.value_a, ', ', self.value_b, ']')
        print('Número de iteraciones a evaluar: ', self.iterations)
        print('Número de decimales que se tomaran en cuenta: ', self.decimals)
        print('')
        #
        for it in range(self.iterations):
            Fa_tmp = self.evaluate(self.function, self.value_a)
            Fa = round(Fa_tmp, self.decimals)
            Fb_tmp = self.evaluate(self.function, self.value_b)
            Fb = round(Fb_tmp, self.decimals)
            xi_tmp = self.evaluate_xi(Fa, Fb)
            xi = round(xi_tmp, self.decimals)
            Fxi_temp = self.evaluate(self.function, xi)
            Fxi = round(Fxi_temp, self.decimals)
            table.add_row([it, self.value_a, self.value_b, Fa, Fb, xi, Fxi])
            if Fa > 0 and Fb > 0:
                break_state = 1
                break
            elif Fa < 0 and Fb < 0:
                break_state = 1
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
        if break_state == 1:
            print('')
            print('Los valores ingresados o la función no cumplen con los requisitos válidos para la solución del ',
                  'método de la Regla Falsa')

    def menu(self):
        print('')
        print('[METODO DE REGLA FALSA]')
        print('')
        print('1. Iniciar con valores ya definidos')
        print('2. Ingresar valores')
        print('')
        option = input('[por defecto 1]: ')
        if int(option) == 1:
            self.method()
        elif int(option) == 2:
            print('')
            for i in range(5):
                print('> Ingrese los valores a evaluar')
                function = input('[función]: ')
                value_a = input('[intérvalo A]: ')
                value_b = input('[intérvalo B]: ')
                iterations = input('[# de iteraciones]: ')
                decimals = input('[# de decimales a tener en cuenta]: ')
                print('')
                if self.validate(function, 0):
                    self.function = function
                    self.value_a = int(value_a)
                    self.value_b = int(value_b)
                    self.iterations = int(iterations) + 1
                    self.decimals = int(decimals)
                    self.method()
                    break
                else:
                    print('La función ingresada no es válida para operar, intentelo de nuevo.')
        else:
            print('> Ingrese una opción válida.')


regla_falsa = ReglaFalsa('pow(x, 2) - 2', 0, 2, 5, 2)
regla_falsa.menu()

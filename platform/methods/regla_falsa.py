from math import *
from prettytable import PrettyTable


class ReglaFalsa:
    def __init__(self, function, value_a, value_b, iterations, decimals):
        self.function = function
        self.value_a = value_a
        self.value_b = value_b
        self.iterations = iterations
        self.decimals = decimals

    def method(self):
        return 0


regla_falsa = ReglaFalsa('2 * x + pow(x, 3) - 10', 1, 2, 5, 2)
regla_falsa.method()

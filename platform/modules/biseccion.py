from math import *
from flask import request, flash
from ast import literal_eval

def init(function, a, b, iteratins, decimals):
    if validate_function(function, 0):
        flash('La función ingresada es válida', 'success')
    else:
        flash('La función ingresada es INVÁLIDA', 'warning')

def validate_function(function, x):
    try:
        eval(function)
        return True
    except (SyntaxError, ValueError) as execption:
        print(execption)
        return False
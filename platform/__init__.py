from flask import Flask, render_template, request, flash
from math import *

platform = Flask(__name__)


def validate_function(function, x):
    try:
        eval(function)
        return True
    except (SyntaxError, ValueError, NameError) as execption:
        print('[EXCEPTION]:', execption)
        return False

@platform.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@platform.route('/')
def main():
    return render_template('index.html')


@platform.route('/biseccion', methods=['GET', 'POST'])
def biseccion():
    solve = False
    if request.method == "POST":
        function = request.form.get('function')
        if validate_function(function, 0):
            flash('La función ingresada es válida', 'success')
            solve = True
            solve_info = {'function' : function, 'value_a' : request.form.get('value-a'),
                          'value_b' : request.form.get('value-b'), 'iterations' : request.form.get('iterations'),
                          'decimals' : request.form.get('decimals')}
            return render_template('biseccion.html', solve=solve, solve_info=solve_info)
        else:
            flash('La función ingresada NO es válida', 'warning')
            return render_template('biseccion.html')


@platform.route('/regla-falsa')
def regla_falsa():
    return render_template('regla-falsa.html')


@platform.route('/newton-rapshon')
def newton_rapshon():
    return render_template('newton-rapshon.html')


@platform.route('/secante')
def secante():
    return render_template('secante.html')
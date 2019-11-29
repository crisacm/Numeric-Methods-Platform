from flask import Flask, render_template, request, flash
from platform.modules import biseccion
from math import sin, cos, tan, fabs, sqrt, log, pi, e, pow

platform = Flask(__name__)


@platform.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@platform.route('/')
def main():
    return render_template('index.html')


@platform.route('/biseccion', methods=['GET', 'POST'])
def biseccion():
    if request.method == "POST":
        function = request.form.get('function')
        if biseccion.validate_function(function):
            flash('Función valida!', 'success')
        else:
            flash('Función invalida!', 'warning')
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
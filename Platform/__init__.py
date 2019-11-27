from flask import Flask, render_template, request
from platform.modules.biseccion import Form, validate_function

platform = Flask(__name__)


@platform.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@platform.route('/')
def main():
    return render_template('index.html')


@platform.route('/biseccion', methods=['GET', 'POST'])
def biseccion():
    form = Form()
    if request.method == "POST" or form.validate():
        if validate_function(form.functionField.data):
            return True
    return render_template('biseccion.html', form=form)


@platform.route('/regla-falsa')
def regla_falsa():
    return render_template('regla-falsa.html')


@platform.route('/newton-rapshon')
def newton_rapshon():
    return render_template('newton-rapshon.html')


@platform.route('/secante')
def secante():
    return render_template('secante.html')
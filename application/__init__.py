from flask import Flask, render_template

application = Flask(__name__)


@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@application.route('/')
def main():
    return render_template('index.html')


@application.route('/biseccion')
def biseccion():
    return render_template('biseccion.html')


@application.route('/regla-falsa')
def regla_falsa():
    return render_template('regla-falsa.html')


@application.route('/newton-rapshon')
def newton_rapshon():
    return render_template('newton-rapshon.html')


@application.route('/secante')
def secante():
    return render_template('secante.html')
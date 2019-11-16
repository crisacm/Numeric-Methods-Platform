import flask as flask


application = flask.Flask(__name__)


@application.route('/')
def main():
    return flask.render_template('index.html')

@application.route('/biseccion')
def biseccion():
    return flask.render_template('biseccion.html')

@application.route('/newton-rapshon')
def newtonRapshon():
    return flask.render_template('newton-rapshon.html')

@application.route('/regla-falsa')
def reglaFalsa():
    return flask.render_template('regla-falsa.html')

@application.route('/secante')
def secante():
    return flask.render_template('secante.html')

if __name__ == "__main__":
    application.run(debug=True)

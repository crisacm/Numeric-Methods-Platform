import flask as flask
from services import routes

application = flask.Flask(__name__)
defineRoutes = routes()

if __name__ == "__main__":
    application.run(debug=True)

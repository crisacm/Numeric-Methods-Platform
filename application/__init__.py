from flask import Flask, render_template

application = Flask(__name__)


@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@application.route('/')
def main():
    return render_template('index.html')

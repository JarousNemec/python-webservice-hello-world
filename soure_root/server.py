import os
from flask import Flask, send_from_directory, Response, render_template, request, redirect, url_for
from waitress import serve

import logging


def flask_app():
    app = Flask(__name__)

    @app.route("/")
    def client():
        return "Hello world"

    @app.route('/api/ping')
    def ping():
        return Response(status=200)

    return app


def server():
    manager_app = flask_app()
    logging.info("Serving on http://localhost:80")
    serve(manager_app, port=80)

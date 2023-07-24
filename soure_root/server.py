import os
from flask import Flask, send_from_directory, Response, render_template, request, redirect, url_for
from waitress import serve


def flask_app():
    app = Flask(__name__)

    @app.route("/")
    def client():
        print("default...............................")
        return "Hello world"

    @app.route('/api/ping')
    def ping():
        print("Ping...............................")
        return Response(status=200)

    return app


def server():
    manager_app = flask_app()
    print("Started...............................")
    serve(manager_app, port=80)

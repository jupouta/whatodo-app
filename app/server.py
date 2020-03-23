from flask import Flask

import json
import os

import routes
from database import Database
from todo import Todo


def create_app():
    app = Flask(__name__)
    #app.config.from_object("settings")

    app.add_url_rule("/", view_func=routes.home, methods=["GET", "POST"])
    app.add_url_rule("/todos", view_func=routes.todos_page)
    
    data = read_json()

    db = Database()
    db.add_todos(data)
    app.config["db"] = db

    return app

def read_json():
    with open(os.getcwd() + '/app/static/data.json') as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    app = create_app()
    #port = app.config.get("PORT", 5000)
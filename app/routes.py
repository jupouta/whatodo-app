#from flask import Flask
#app = Flask(__name__)

from flask import render_template, current_app, request, redirect, url_for

from database import Database
from todo import Todo

#@app.route('/')
def home():
    db = current_app.config["db"]
    if request.method == "GET":
        todo = db.random_todo()
        return render_template("hello.html", data=todo)
    else:
        return redirect(url_for('home'))

#@app.route("/todos")
def todos_page():
    db = current_app.config["db"]
    todos = db.get_todos()
    return render_template("todos.html", data=todos)

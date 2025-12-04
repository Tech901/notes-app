"""
A simple Flask application for managing notes.

It uses the same Notes class as our notes.py module for data management.

For more details on Flask, visit: https://flask.palletsprojects.com/en/stable/
"""

from flask import Flask
from flask import request, render_template, redirect, url_for

from notes import Notes

app = Flask(__name__)

@app.route("/")
def index():
    notes = Notes()
    response = render_template("index.html", notes=notes.get_notes())
    notes.close()
    return response


@app.route("/create", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        notes = Notes()
        notes.add_note(request.form["content"])
        notes.close()
        # redirect after Post
        return redirect(url_for("index"))
    # GET requests
    return render_template("create.html")


@app.route("/delete/<int:note_id>", methods=["GET", "POST"])
def delete_note(note_id):
    notes = Notes()
    if request.method == "POST":
        notes.remove_note(note_id)
        return redirect(url_for("index")) # redirect after POST

    # GET requests
    return render_template("confirm.html", note=notes.get_note(note_id))

# IDEAS for updates
# 1. Make a route for a single note, e.g. /<int:note_id>
# 2. Make an Edit route, e.g. /edit/<int:note_id>
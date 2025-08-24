from flask import render_template

from ..main import main

@main.route('/')
def index():
    return render_template("index.html.j2")

@main.route('/spectacles')
def spectacles():
    return render_template("spectacles.html.j2")

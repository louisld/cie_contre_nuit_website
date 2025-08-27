from flask import render_template

from ..main import main

from app.main.models import Project

@main.route('/')
def index():
    projects = Project.query.all()

    return render_template(
        "index.html.j2",
        projects=projects
    )

@main.route('/la-compagnie')
def troupe():
    return render_template("troupe.html.j2")

@main.route('/nos-projets')
def projects():
    return render_template("projects.html.j2")

@main.route('/contact')
def contact():
    return render_template("contact.html.j2")

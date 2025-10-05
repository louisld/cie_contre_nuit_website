import json
from pathlib import Path

import flask
from flask import render_template

from markdown import markdown

from ..main import main
from app.main.models import Info, Member, Project

TROUPE_DESCRIPTION_PATH = Path("app/static/main/troupe/uploads/description.md")
PLAY_POSTER_DESC = {
    "path": Path("app/static/main/project/uploads/"),
    "filename": "_poster_desc.md"
}

@main.route('/')
def index():
    projects = Project.query.order_by(Project.is_future.desc(), Project.start_date.desc()).all()

    return render_template(
        "index.html.j2",
        projects=projects
    )

@main.route('/la-compagnie')
def troupe():
    members = Member.query.order_by(Member.display_order.desc()).all()

    description = ""
    if TROUPE_DESCRIPTION_PATH.is_file():
        with open(TROUPE_DESCRIPTION_PATH, "r") as f:
            description = markdown(f.read(), extensions=['extra'])

    return render_template(
        "troupe.html.j2",
        description=description,
        members=members
    )

@main.route('/nos-projets')
def projects():
    projects = Project.query.order_by(Project.is_future.desc(), Project.start_date.desc()).all()

    return render_template(
        "projects.html.j2",
        projects=projects
    )

@main.route('/contact')
def contact():

    return render_template(
        "contact.html.j2",
        info = Info()
    )

@main.route('/piece/<string:short_title>')
def play(short_title: str):
    project: Project | None = Project.query.filter_by(short_title=short_title).first()

    if project is None:
        return flask.abort(404, description="Le projet n'existe pas.")

    return render_template(
        "play.html.j2",
        project = project
    )


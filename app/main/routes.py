import json
from pathlib import Path

from flask import render_template

from markdown import markdown

from ..main import main
from app.main.models import Info, Member, Project

TROUPE_DESCRIPTION_PATH = Path("app/static/main/troupe/uploads/description.md")

@main.route('/')
def index():
    projects = Project.query.order_by(Project.is_future.desc(), Project.start_date.desc()).all()

    return render_template(
        "index.html.j2",
        projects=projects
    )

@main.route('/la-compagnie')
def troupe():
    members = Member.query.all()

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

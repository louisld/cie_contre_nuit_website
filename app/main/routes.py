import json

from flask import render_template

from ..main import main

from app.main.models import Info, Member, Project

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

    return render_template(
        "troupe.html.j2",
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

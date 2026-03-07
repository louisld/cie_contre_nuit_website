import os

import flask
from flask import render_template, current_app

from flask_login import login_required

from ..admin import admin
from app.main.models import Member
from app.admin.forms import MemberEditForm

from app.extensions import db

@admin.route("/dashboard")
@login_required
def dashboard():
    return render_template(
        "dashboard.html.j2"
    )

@admin.route("index")
@login_required
def index():
    return render_template(
        "index_edit.html.j2"
    )

@admin.route("/troupe")
@login_required
def troupe():
    members = Member.query.order_by(Member.display_order.desc()).all()

    return render_template(
        "troupe_edit.html.j2",
        members=members
    )

@admin.route("/troupe/member/<int:id>", methods=["POST", "GET"])
@login_required
def member(id: int):
    member = Member.query.get(id)

    if member is None:
        return flask.abort(404, description="Le membre n'existe pas.")
    
    member_form = MemberEditForm()
    if member_form.validate_on_submit():
        member.first_name = member_form.first_name.data
        member.last_name = member_form.last_name.data
        member.role = member_form.role.data
        member.display_order = member_form.display_order.data

        db.session.commit()

        print(member_form.cover_img.data)
        if member_form.cover_img.data:
            member_form.cover_img.data.save(os.path.join(
                current_app.root_path,
                "static/main/troupe/uploads/",
                f"{member.id}_cover.jpg"
            ))
        if member_form.name_img.data:
            member_form.name_img.data.save(os.path.join(
                current_app.root_path,
                "static/main/troupe/uploads/",
                f"{member.id}_name.png"
            ))
    
    return render_template(
        "member_edit.html.j2",
        member=member,
        member_form=member_form
    )
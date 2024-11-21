import sys
from flask import render_template, Blueprint, redirect, url_for, flash, jsonify
from sqlalchemy import desc
from flask_login import login_required
from flaskr import db
from flaskr.models import SchoolSession, Subject, Student, Result
from flaskr.managements.forms import SchoolSessionForm, SubjectForm
from flaskr.auths.utils import requires_role

managements = Blueprint("managements", __name__)


@managements.route("/dashboard")
@login_required
@requires_role("admin")
def dashboard():
    return render_template("dashboard.html")


@managements.route("/school-session")
@login_required
@requires_role("admin")
def school_session():
    return render_template("school-session.html")


@managements.route("/new-session", methods=["GET", "POST"])
@login_required
@requires_role("admin")
def new_session():
    current_session = SchoolSession.query.order_by(
        desc(SchoolSession.start_date)
    ).first()
    current_session = current_session.session if current_session else "2024/2025"
    form = SchoolSessionForm()
    form.session.choices = SchoolSession.school_session()
    form.confirm_session.choices = SchoolSession.school_session()
    if form.validate_on_submit():
        session = SchoolSession(
            session=form.session.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
        )
        db.session.add(session)
        db.session.commit()
        students = Student.query.all()
        for student in students:
            if student.student_class == "JS1":
                student.student_class = "JS2"
            elif student.student_class == "JS2":
                student.student_class = "JS3"
            elif student.student_class == "JS3":
                student.student_class = "SS1"
            elif student.student_class == "SS1":
                student.student_class = "SS2"
            elif student.student_class == "SS2":
                student.student_class = "SS3"
            elif student.student_class == "SS3":
                student.student_class = "Graduated"
            db.session.commit()
        flash(f"{session.session} has been created as the current session!", "success")
        return redirect(url_for("managements.new_session"))
    return render_template(
        "new-session.html", current_session=current_session, form=form
    )


@managements.route("/subjects-dashboard")
@login_required
@requires_role("admin")
def subject_view():
    return render_template("subjects-dashboard.html")


@managements.route("/subjects")
@login_required
@requires_role("admin")
def get_subjects():
    subjects = Subject.query.order_by(Subject.name).all()
    return render_template("subjects.html", subjects=subjects)


@managements.route("/create-subject", methods=["GET", "POST"])
@login_required
@requires_role("admin")
def subject_create_view():
    form = SubjectForm()
    if form.validate_on_submit():
        name = form.name.data.strip()
        subjects = Subject.query.all()
        subject_exist = False
        for subject in subjects:
            if subject.name.lower() == name.lower():
                subject_exist = True
        if not subject_exist:
            subject = Subject(name=name, class_range=form.class_range.data)
            db.session.add(subject)
            db.session.commit()
            flash(f"{form.name.data} has been added as a new subject!", "success")
            return render_template("subject-create.html", form=form)
        else:
            flash(f"{name} already exist in the database", "info")
            return redirect(url_for("managements.subject_create_view"))
    return render_template("subject-create.html", form=form)


@managements.route("/delete-subject-score/<int:score_id>", methods=["DELETE"])
@login_required
@requires_role("admin")
def subject_score_delete(score_id):
    print(score_id)
    subject_score = Result.query.get(score_id)
    if subject_score:
        db.session.delete(subject_score)
        db.session.commit()
    return jsonify({"message": "Item deleted successfully"}), 200


@managements.route("/edit-subject/<int:subject_id>", methods=["GET", "POST"])
@login_required
@requires_role("admin")
def subject_edit_view(subject_id):
    form = SubjectForm()
    if form.validate_on_submit():
        name = form.name.data.strip()
        subject = Subject.query.get(subject_id)
        results = Result.query.all()
        if subject.name:
            for result in results:
                if result.subject.lower() == subject.name.lower():
                    result.subject = name.lower()
            subject.name = name
        if subject.class_range:
            subject.class_range = form.class_range.data
        db.session.commit()
        flash(f"{form.name.data} has been updated!", "success")
        return redirect(url_for("managements.get_subjects"))
    subject = Subject.query.get(subject_id)
    form.name.data = subject.name
    form.class_range.data = subject.class_range
    return render_template("edit-subject.html", form=form)


@managements.route("/delete-subject/<int:subject_id>", methods=["DELETE"])
@login_required
@requires_role("admin")
def delete_subject(subject_id):
    subject = Subject.query.get(subject_id)
    if subject:
        db.session.delete(subject)
        db.session.commit()
        return jsonify({"message": "subject deleted successfully!"}), 200

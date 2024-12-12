from flask import redirect, render_template, url_for, request, Blueprint, flash, session
from flask_login import login_user, current_user, logout_user
from flaskr import bcrypt
from flaskr.auths.forms import LoginForm
from flaskr.models import Management, Teacher, Student

auths = Blueprint("auths", __name__)


# TODO: to implement for teachers and student login
@auths.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        if current_user.role == "admin":
            flash("You are already logged in!", "info")
            return redirect(url_for("managements.dashboard"))
        elif current_user.role == "teacher":
            teacher = Teacher.query.get(current_user.id)
            teacher_id = teacher.id
            flash("You are already logged in!", "info")
            return redirect(url_for("teachers.teacher_profile", teacher_id=teacher_id))
        elif current_user.role == "student":
            student = Student.query.get(current_user.id)
            student_id = student.id
            flash("You are already logged in!", "info")
            return redirect(url_for("students.student_profile", std_id=student_id))
        else:
            return redirect(url_for("main.home_page"))

    form = LoginForm()
    if form.validate_on_submit():
        print(f"submitted email is {form.email.data}")
        print(f"submitted password is {form.password.data}")
        management = Management.query.filter_by(email=form.email.data).first()
        teacher = Teacher.query.filter_by(email=form.email.data).first()
        student = Student.query.filter_by(email=form.email.data).first()
        if management and bcrypt.check_password_hash(
            management.password, form.password.data
        ):
            print(f"got management email: {management.email}")
            session["email"] = management.email
            login_user(management, remember=form.remember.data)
            flash(
                f"Welcome back Admin!",
                "info",
            )
            next_page = request.args.get("next")
            return (
                redirect(next_page)
                if next_page
                else redirect(url_for("managements.dashboard"))
            )
        elif teacher and bcrypt.check_password_hash(
            teacher.password, form.password.data
        ):
            session["email"] = teacher.email
            login_user(teacher, remember=form.remember.data)
            flash(
                f"Welcome back {teacher.title.title()} {teacher.last_name.title()}!",
                "success",
            )
            return redirect(url_for("teachers.teacher_profile", teacher_id=teacher.id))
        elif student and bcrypt.check_password_hash(
            student.password, form.password.data
        ):
            session["email"] = student.email
            login_user(student, remember=form.remember.data)
            flash(
                f"Welcome back {student.last_name.title()} {student.first_name.title()}!",
                "success",
            )
            return redirect(url_for("students.student_profile", std_id=student.id))
        else:
            flash("Incorrect Email or Password!", "danger")
            return redirect(url_for("auths.login"))
    print(f"Access login page")
    return render_template("login.html", form=form)


@auths.route("/logout")
def logout():
    logout_user()
    session.clear()
    return redirect(url_for("main.home_page"))

import os
from sqlalchemy import desc
from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_required
from flaskr import bcrypt, db
from flaskr.models import Teacher
from flaskr.teachers.forms import TeacherRegisterationForm, TeacherUpdateForm
from flaskr.auths.utils import requires_role, save_and_resize_picture, upload_to_s3


teachers = Blueprint("teachers", __name__)

S3_BUCKET = os.environ.get("S3_BUCKET")
S3_REGION = os.environ.get("S3_REGION")


def teacher_identification():
    teacher = Teacher.query.order_by(desc(Teacher.date_joined)).first()
    if teacher:
        recent_teacher_serial = int(teacher.tID[11:])
        teacher_serial = recent_teacher_serial + 1
    else:
        teacher_serial = 1
    if teacher_serial < 10:
        tID = "ISMC2024TCH" + "00" + str(teacher_serial)
    elif teacher_serial < 100:
        tID = "ISMC2024TCH" + "0" + str(teacher_serial)
    else:
        tID = "ISMC2024TCH" + str(teacher_serial)
    return tID


@teachers.route("/teachers-dashboard")
@login_required
@requires_role("admin")
def teachers_dashboard():
    return render_template("teachers-dashboard.html")


@teachers.route("/teacher-profile/<int:teacher_id>")
@login_required
@requires_role("teacher")
def teacher_profile(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    return render_template("teacher-profile.html", teacher=teacher)


@teachers.route("/register-teacher", methods=["GET", "POST"])
@login_required
@requires_role("admin")
def teacher_register():
    form = TeacherRegisterationForm()
    if form.validate_on_submit():
        if form.picture.data:
            try:
                picture_fn, temp_file_path = save_and_resize_picture(form.picture.data)
                s3_url = upload_to_s3(temp_file_path, picture_fn, S3_BUCKET, S3_REGION)
                print(f"Image uploaded successfully! URL: {s3_url}", "success")
            except Exception as e:
                print(f"Error uploading image: {e}", "danger")
            password = form.last_name.data.lower() + "_ismc24"
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            tID = teacher_identification()
            teacher = Teacher(
                first_name=form.first_name.data,
                middle_name=form.middle_name.data,
                last_name=form.last_name.data,
                title=form.title.data,
                sex=form.sex.data,
                email=form.email.data,
                section=form.section.data,
                phone_number=form.phone_number.data,
                address=form.address.data,
                picture=picture_fn,
                password=hashed_password,
                tID=tID,
            )
        else:
            password = form.last_name.data.lower() + "_ismc24"
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            tID = teacher_identification()
            teacher = Teacher(
                first_name=form.first_name.data,
                middle_name=form.middle_name.data,
                last_name=form.last_name.data,
                title=form.title.data,
                sex=form.sex.data,
                email=form.email.data,
                section=form.section.data,
                phone_number=form.phone_number.data,
                address=form.address.data,
                password=hashed_password,
                tID=tID,
            )
        db.session.add(teacher)
        db.session.commit()
        flash(
            f"{form.first_name.data} {form.last_name.data} has been registered as a teacher!",
            "success",
        )
        return redirect(url_for("teachers.teacher_register"))
    return render_template("register-teacher.html", form=form)


@teachers.route("/update-teacher-profile/<int:teacher_id>", methods=["GET", "POST"])
@login_required
def update_teacher_profile(teacher_id):
    form = TeacherUpdateForm()
    teacher = Teacher.query.get(teacher_id)
    if form.validate_on_submit():
        try:
            if form.first_name.data:
                teacher.first_name = form.first_name.data
            if form.last_name.data:
                teacher.last_name = form.last_name.data
                hashed_password = bcrypt.generate_password_hash(
                    form.last_name.data.lower()
                ).decode("utf-8")
                teacher.password = hashed_password
            if form.middle_name.data:
                teacher.middle_name = form.middle_name.data
            if form.title.data:
                teacher.title = form.title.data
            if form.sex.data:
                teacher.sex = form.sex.data
            if form.email.data:
                teacher.email = form.email.data
            if form.section.data:
                teacher.section = form.section.data
            if form.phone_number.data:
                teacher.phone_number = form.phone_number.data
            if form.address.data:
                teacher.address = form.address.data
            if form.picture.data:
                try:
                    picture_fn, temp_file_path = save_and_resize_picture(
                        form.picture.data
                    )
                    print(temp_file_path, picture_fn)
                    s3_url = upload_to_s3(
                        temp_file_path, picture_fn, S3_BUCKET, S3_REGION
                    )

                    print(f"Image uploaded successfully! URL: {s3_url}", "success")
                except Exception as e:
                    print(f"Error uploading image: {e}", "danger")
                finally:
                    teacher.picture = picture_fn
            # if form.picture.data:
            #     teacher.picture = save_picture(form.picture.data)
            db.session.commit()
            flash(
                f"{teacher.last_name} {teacher.first_name} profile has been updated successfully!",
                "success",
            )
            return redirect(url_for("teachers.teacher_profile", teacher_id=teacher_id))
        except:
            flash("There was a problem updating the teachers profile!", "danger")
            return redirect(url_for("teachers.teacher_profile", teacher_id=teacher_id))

    form.first_name.data = teacher.first_name
    form.last_name.data = teacher.last_name
    form.middle_name.data = teacher.middle_name
    form.email.data = teacher.email
    form.sex.data = teacher.sex
    form.title.data = teacher.title
    form.section.data = teacher.section
    form.address.data = teacher.address
    form.phone_number.data = teacher.phone_number
    return render_template("teacher-update-form.html", form=form)


@teachers.route("/teachers")
@login_required
@requires_role("admin")
def get_teachers():
    teachers = Teacher.query.all()
    return render_template("teachers.html", teachers=teachers)


@teachers.route("/delete-teacher/<int:teacher_id>", methods=["DELETE"])
@login_required
@requires_role("admin")
def delete_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if teacher:
        try:
            db.session.delete(teacher)
            db.session.commit()
            flash(
                f"{teacher.last_name} {teacher.first_name} profile has been deleted!",
                "info",
            )
            return render_template("teachers-dashboard.html")
        except:
            flash(
                f"There was a problem deleting {teacher.last_name} {teacher.first_name} profile!",
                "danger",
            )
            return redirect(url_for("teachers.teachers_dashboard"))
    flash(
        f"There was a problem deleting {teacher.last_name} {teacher.first_name} profile!",
        "danger",
    )
    return redirect(url_for("teachers.teachers_dashboard"))

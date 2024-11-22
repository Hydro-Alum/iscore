import os
import secrets
from PIL import Image, ImageOps
from flask import abort, current_app
from functools import wraps
from flask_login import current_user


def requires_role(role):
    def requires_role_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if current_user.role == role or current_user.role == "admin":
                print("current_user is:", current_user.role)
                return f(*args, **kwargs)
            else:
                abort(403)

        return wrapper

    return requires_role_decorator


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/profile_pics", picture_fn
    )
    output_size = (125, 125)
    img = Image.open(form_picture)
    img = ImageOps.exif_transpose(img)
    img.thumbnail(output_size)
    img.save(picture_path)
    return picture_fn

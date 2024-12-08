import os
import tempfile
import boto3
import secrets
from werkzeug.utils import secure_filename
from botocore.exceptions import NoCredentialsError, ClientError
from PIL import Image, ImageOps
from flask import abort, current_app
from functools import wraps
from flask_login import current_user


def requires_role(role):
    def requires_role_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if current_user.role == role or current_user.role == "admin":
                return f(*args, **kwargs)
            else:
                abort(403)

        return wrapper

    return requires_role_decorator


# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(
#         current_app.root_path, "static/profile_pics", picture_fn
#     )
#     output_size = (125, 125)
#     img = Image.open(form_picture)
#     img = ImageOps.exif_transpose(img)
#     img.thumbnail(output_size)
#     img.save(picture_path)
#     return picture_fn


def upload_to_s3(file_path, file_name, bucket_name, region):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        region_name=region,
    )

    try:
        s3.upload_file(file_path, bucket_name, f"profile_pics/{file_name}")
        print(f"File uploaded successfully to S3: {file_name}")
        s3_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{file_name}"
        print(f"S3 URL: {s3_url}")
        return s3_url
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except NoCredentialsError:
        print("Error: AWS credentials not available.")
        raise
    except ClientError as e:
        print(f"ClientError: {e}")
        raise


# Save and resize picture before uploading
def save_and_resize_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, "profile_pics", secure_filename(picture_fn))
    os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
    # temp_file_path = os.path.join(
    #     current_app.root_path, "static\profile_pics", picture_fn
    # )

    # Resize the image
    output_size = (125, 125)
    img = Image.open(form_picture)
    img = ImageOps.exif_transpose(img)
    img.thumbnail(output_size)
    img.save(temp_file_path)
    print(f"Resized image saved temporarily: {temp_file_path}")
    return picture_fn, temp_file_path

from flask import render_template, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home_page():
    return render_template("index.html")

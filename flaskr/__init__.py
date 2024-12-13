from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from flask_session import Session
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskr.config import DevelopmentConfig, ProductionConfig


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auths.login"
# login_manager.login_message = "Redirected for no reason"
# login_manager.login_message_category = "info"

from flaskr import models


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config["SESSION_SQLALCHEMY"] = db
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Session(app)

    from flaskr.main.routes import main
    from flaskr.managements.routes import managements
    from flaskr.auths.routes import auths
    from flaskr.students.routes import students
    from flaskr.teachers.routes import teachers

    app.register_blueprint(main)
    app.register_blueprint(managements)
    app.register_blueprint(auths)
    app.register_blueprint(students)
    app.register_blueprint(teachers)

    return app

from datetime import datetime
from email.message import Message
import hashlib
from itertools import accumulate
from os import access
from unicodedata import name

from flask import (
    Blueprint,
    Flask,
    flash,
    abort,
    jsonify,
    render_template, 
    redirect, 
    session, 
    url_for, 
    request
)
from flask_login import (
    LoginManager, 
    UserMixin, 
    login_user, 
    login_required, 
    logout_user, 
    current_user
)

from itsdangerous import SignatureExpired, URLSafeTimedSerializer
from flask_mail import Mail, Message

from .db.database import db
from .db.models import Usuario, Curso, Lleva, Post

from . import forms 
from werkzeug.utils import secure_filename


# GLOBAL VARIABLES
api = Blueprint('login', __name__, template_folder='templates', static_folder='static')
s = URLSafeTimedSerializer('ClavePocoSecreta')
mail = Mail()

# AUXILIARY FUNCTIONS

def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_email):
        return Usuario.query.get(user_email)

def configure_mails(app):
    mail.init_app(app)   

# API ENDPOINTS

@api.route("/", methods=['GET'])
def index():
    return jsonify({
        'success': True
    })


@api.route("/example-endpoint", methods=['GET'])
def example():
    return jsonify({
        'msg': "CORS available: Message from Flask server"
    })

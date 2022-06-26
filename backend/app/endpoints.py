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


@api.route("/user", methods=['GET'])
def get_user():
    print(f'{type(request.form)} -> {request.form}')
    err_description = ""
    try:
        form = forms.LoginF(request.form)
        username = form.username.data
        password = form.password.data

        usuario =  Usuario.query.filter_by(username = username).first()
        print(f"user -> {usuario}")
        
        if  usuario is not None and \
            usuario.check_password(password) and \
            usuario.confirmacion:

            login_user(usuario, remember=True)
            return jsonify({
                'success': True,
                'endpoint': '/user',
                'method': 'GET',
                'user': usuario.get_attributes()
            })    
        else: 
            if usuario is None:
                err_description = "user not found"
            elif not usuario.check_password(password):
                err_description = "incorrect password"
            elif not usuario.confirmacion:
                err_description = "unconfirmed user"
            abort(500)
    except Exception as e:
        print(f"EXCEPTION: {e}")
        abort(500, description=err_description)


@api.route("/user", methods=['POST'])
def create_user():
    print(f'{type(request.form)} -> {request.form}')

    try:
        form = forms.SignUpF(request.form)
        new_user =  Usuario(form.email.data, 
                            form.username.data, 
                            form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'success': True,
            'code': 200,
            'endpoint': '/user',
            'method': 'POST'
        })
    except Exception as e:
        db.session.rollback()
        print(f"EXCEPTION: {e}")
        abort(500)
    finally:
        db.session.close()


@api.route("/user", methods=['PATCH'])
def update_user():
    return jsonify({
        'success': True,
        'endpoint': '/user',
        'method': 'PATCH'
    })


@api.route("/user", methods=['DELETE'])
def delete_user():
    return jsonify({
        'success': True,
        'endpoint': '/user',
        'method': 'DELETE'
    })

@api.route("/example-endpoint", methods=['GET'])
def example():
    return jsonify({
        'msg': "CORS available: Message from Flask server"
    })

# ERROR HANDLER
@api.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'code': 404,
        'message': 'resource not found'
    }), 404

@api.errorhandler(500)
def server_error(error):
    return jsonify({
        'success': False,
        'code': 500,
        'message': 'server error',
        'description': str(error)
    }), 500

@api.errorhandler(405)
def server_error(error):
    return jsonify({
        'success': False,
        'code': 405,
        'message': 'method not allowed'
    }), 405

@api.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'code': 422,
        'message': 'unprocessable'
    }), 422

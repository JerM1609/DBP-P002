from datetime import datetime
import email
from email.message import Message
import hashlib
from itertools import accumulate
import os
from urllib import response

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
from sqlalchemy import Identity

from .db.database import db
from .db.models import Usuario, Curso, Lleva, Post

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, get_jwt_identity, jwt_required, set_access_cookies, set_refresh_cookies, JWTManager, unset_jwt_cookies

from . import forms 
from werkzeug.utils import secure_filename



# GLOBAL VARIABLES
api = Blueprint('login', __name__, template_folder='templates', static_folder='static')
s = URLSafeTimedSerializer('ClavePocoSecreta')
mail = Mail()


# AUXILIARY FUNCTIONS

GOOGLE_CLIENT_ID = '59012120039-54jvcg23a2met0bl2oheigt0sfrdn9mu.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'


def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_email):
        return Usuario.query.get(user_email)

def configure_mails(app):
    mail.init_app(app)   

jwt = None
def init_jwt(app): 
    jwt = JWTManager(app)

# API ENDPOINTS
ITEMS_PER_PAGE=10

def paginate_items(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page-1)*ITEMS_PER_PAGE
    end = start+ITEMS_PER_PAGE

    items = [item.get_attributes() for item in selection]
    current_items = items[start:end]
    return current_items


# API ENDPOINTS

@api.route("/", methods=['GET'])
def index():
    return jsonify({
        'success': True
    })




@api.route("/sign-up", methods=['POST'])
def create_user():
    try:
        body = request.get_json()

        username = body.get('username', None)
        email = body.get('email', None)
        password = body.get('password', None)
        search = body.get('search', None)

        if username is None or email is None or password is None:
            abort(422)
        
        new_user =  Usuario(email, 
                            username, 
                            password)
        new_user_id = new_user.insert()
        
        access_token = create_access_token(identity=new_user.email)
        refresh_token = create_refresh_token(identity=new_user.email)
        
        response = jsonify({
                'success': True,
                'code': 200,
                'endpoint': '/sign-up',                
                'access_token': access_token,
                'method': 'POST',
                'created': new_user_id,
            })
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response

    except Exception as e:
        print(f"EXCEPTION: {e}")
        abort(500)

@api.route("/log-in", methods=['POST'])
def log_in():
    err_description = ""
    try:
        body = request.get_json()
        email = body.get("email", None)
        password = body.get("password", None)
        if email is None: 
            abort(401)

        usuario =  Usuario.query.filter_by(email = email).first()
        print(f"user -> {usuario}")
        
        if  usuario is not None and \
            usuario.check_password(password):
            access_token = create_access_token(identity=usuario.email)
            refresh_token = create_refresh_token(identity=usuario.email)

            response = jsonify({
                'code': 200,
                'success': True,
                'endpoint': '/login',                
                'access_token': access_token,
                'method': 'GET',
                'user': usuario.get_attributes()
            })
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            print(request.cookies.get('code'))
            return response
        else: 
            if usuario is None:
                err_description = "user not found"
            elif not usuario.check_password(password):
                err_description = "incorrect password"

            abort(500)
    except Exception as e:
        print(f"EXCEPTION: {e}")
        abort(500, description=err_description)

@api.route("/user", methods=['DELETE'])
@jwt_required()
def delete_user_by_id():
    error_404 = False
    email = get_jwt_identity()

    print(email)
    try:        
        user = Usuario.query.filter_by(email = email).one_or_none()
        if user is None:
            error_404 = True
            abort(404)
        user.delete()
        return jsonify({
            'success': True,
            'code': 200,
            'deleted': email
            })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/editar-perfil/', methods=['PATCH'])
@jwt_required()
def update_perfil():
    error_404 = False
    try: 
        email = get_jwt_identity()
        userInfo= Usuario.query.filter_by(email = email).one_or_none()
        
        if userInfo is None: 
            error_404 = True
            abort(404)
        body = request.get_json()

        if 'country' in body: 
            userInfo.country = body.get('country')
        if 'institute' in body: 
            userInfo.institute = body.get('institute')
        if 'career' in body: 
            userInfo.career = body.get('career')


        if 'website' in body: 
            userInfo.website = body.get('website')
        if 'github' in body: 
            userInfo.github = body.get('github')                    
        if 'twitter' in body: 
            userInfo.twitter = body.get('twitter')            
        if 'instagram' in body: 
            userInfo.instagram = body.get('instagram')            
        if 'facebook' in body: 
            userInfo.facebook = body.get('facebook')            

        if 'photo' in body:
            userInfo.photo = body.get('photo')
        
        userInfo.update()
        return jsonify({
                'success': True,
                'code': 200,
                'method': 'PATCH',
                'created': email
            })

    except:
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/posts', methods=['GET'])
@jwt_required()
def get_posts():
    idd = get_jwt_identity()
    selection = Post.query.all()
    posts = paginate_items(request, selection)
    if len(posts) == 0:
        abort(404)
    #deberia ser abort? o mas bien enviar lista vacia y que el 
    #front muestre todo vacio?
    return jsonify({
        'success': True,
        'code': 200,
        'endpoint': '/post',
        'method': 'GET',
        'current_user': idd,
        'posts': posts,
        'total_posts': len(selection)
    })


@api.route("/logout", methods=['POST'])
def logout():    
    response = jsonify({
            'success': True,
            'code': 200                                    
            })
    unset_jwt_cookies(response)
    return response








@api.route("/creation_posts", methods=['POST'])
@jwt_required()
def create_post():

    body = request.get_json()
    email = get_jwt_identity()
    titulo = body.get('titulo', None)
    subtitulo = body.get('subtitulo', None)
    contenido = body.get('contenido', None)
    portada = body.get('portada', None)
    search = body.get('search', None)

    if search:
            selection = Post.query.order_by('id').filter(Post.titulo.like('%{}%'.format(search))).all()
            posts = paginate_items(request, selection)
            return jsonify({
                'success': True,
                'posts': posts,
                'total_posts': len(selection)
            })

    if titulo is None or subtitulo is None or contenido is None:
        abort(422)

    #if portada is None: set portada a imagen por default/vacio

    try:
        img = portada
        filename = secure_filename(img)
        
        realname = filename.replace(' ', '_')
        post = Post(
            id=hashlib.md5(titulo.encode()).hexdigest(),
            titulo=titulo,
            subtitulo=subtitulo,
            id_autor=email,
            fecha=datetime.now(),
            contenido=contenido,
            portada = realname        
        )

        new_post_id = post.insert()

        selection = Post.query.order_by('id').all()
        current_posts = paginate_items(request, selection)

        return jsonify({
            'success': True,
            'code': 200,
            'endpoint': '/post',
            'method': 'POST',
            'created': new_post_id,
            'posts' : current_posts,
            'total_posts' : len(selection)
        })
    except Exception as e:
        print(e)
        abort(500)


@api.route("/posts/<post_id>", methods=['PATCH'])
@jwt_required()
def update_post(post_id):
    error_404 = False
    try:
        post = Post.query.filter(Post.id == post_id).one_or_none()

        if post is None:
            error_404 = True
            abort(404)

        body = request.get_json()

        if 'titulo' in body:
            post.titulo = body.get('titulo')
            post.id = hashlib.md5(body.get('titulo').encode()).hexdigest

        if 'subtitulo' in body:
            post.subtitulo = body.get('subtitulo')

        if 'contenido' in body:
            post.contenido = body.get('contenido')

        if 'portada' in body:
            post.portada = body.get('portada')

        post.update()


        return jsonify({
                'success': True,
                'updated_id': post_id
            })
    except:
            if error_404:
                abort(404)
            else:
                abort(500)


@api.route('/posts/<post_id>', methods=['DELETE'])
@jwt_required()
def delete_posts_by_id(post_id):
    error_404 = False
    try:
        post = Post.query.filter_by(id = post_id).one_or_none()
        if post is None:
            error_404 = True
            abort(404)

        post.delete()

        selection = Post.query.order_by('id').all()
        posts = paginate_items(request, selection)

        return jsonify({
            'success': True,
            'code':200,
            'deleted': post_id,
            'post': posts,
            'total_posts': len(selection)
        })

    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)

@api.route('/cursos', methods=['GET'])
@jwt_required()
def get_cursos():

    selection = Curso.query.order_by('id').all()
    cursos = paginate_items(request, selection)

    if len(cursos) == 0:
        abort(404)

    return jsonify({
        'success': True,
        'cursos': cursos,
        'total_cursos': len(cursos)
    })

@api.route('/creation_cursos', methods=['POST'])
@jwt_required()
def create_cursos():
    email = get_jwt_identity()
    body = request.get_json()

    contenido = body.get('contenido',None)
    fecha = datetime.now()
    titulo = body.get('titulo',None)
    subtitulo = body.get('subtitulo',None)
    portada = body.get('portada',None)    
    search = body.get('search',None)

    #creo que falta mejorar el parseado de la portada de acuerdo al forms

    #solo sera search por curso nombre?
    #o por teacher nombre tmb?
    if search:
        selection = Curso.query.order_by('id').filter(Curso.titulo.like('%{}%'.format(search))).all()
        posts = paginate_items(request, selection)
        return jsonify({
            'success': True,
            'cursos': posts,
            'total_cursos': len(posts)
        })

    if contenido is None or titulo is None or subtitulo is None or portada is None:
        abort(422)
        
    #if portada is None, setear a imagen default

    try:
        id_ = hashlib.md5(titulo.encode()).hexdigest()
        curso = Curso(
            id=id_,
            id_teacher = email,
            contenido = contenido,
            fecha = fecha,
            titulo = titulo,
            subtitulo = subtitulo,
            portada = portada
        )
        new_curso_id = curso.insert()

        selection = Curso.query.order_by('id').all()
        cursos = paginate_items(request, selection)
        return jsonify({
            'success': True,
            'code': 200,
            'endpoint': '/post',
            'method': 'POST',
            'created': new_curso_id,
            'cursos' : cursos,
            'total_cursos' : len(selection)            
        })

    except Exception as e:
        print(e)
        abort(500)

@api.route("/cursos/<curso_id>", methods=['PATCH'])
@jwt_required()
def update_curso(curso_id):
    error_404 = False
    try:
        curso = Curso.query.filter(Curso.id == curso_id).one_or_none()

        if curso is None:
            error_404 = True
            abort(404)

        body = request.get_json()

        if 'titulo' in body:
            curso.titulo = body.get('titulo')
            curso.id = hashlib.md5(body.get('titulo').encode()).hexdigest

            
        if 'subtitulo' in body:
            curso.subtitulo = body.get('subtitulo')

        if 'contenido' in body:
            curso.contenido = body.get('contenido')

        curso.update()
        #se rehashearia el id pq el titulo cambio?
        #algun update de fecha?
        #algun update de portada?

        return jsonify({
                'success': True,
                'updated_id': curso_id
            })
    except:
            if error_404:
                abort(404)
            else:
                abort(500)

@api.route('/cursos/<curso_id>', methods=['DELETE'])
@jwt_required()
def delete_cursos_by_id(curso_id):
    email = get_jwt_identity()
    error_404 = False
    try:
        curso = Curso.query.filter(Curso.id == curso_id).one_or_none()
        if curso is None:
            print("Problema con curso delete")
            error_404 = True
            abort(404)

        curso.delete()

        selection = Curso.query.order_by('id').all()
        cursos = paginate_items(request, selection)

        return jsonify({
            'success': True,
            'code':200,
            'deleted': curso_id,
            'cursos': cursos,
            'total_cursos': len(selection)
        })

    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


# ERROR HANDLER
@api.errorhandler(400)
def not_found(error):
    return jsonify({
        'success': False,
        'code': 400,
        'message': 'bad request'
    }), 400


@api.errorhandler(403)
def forbidden(error):
    return jsonify({
        'success': False,
        'code': 403,
        'message': 'forbidden'
    }), 403


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
        'message': 'internal server error'
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



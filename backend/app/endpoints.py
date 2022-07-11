from datetime import datetime
import email
from email.message import Message
import hashlib
from itertools import accumulate
import os

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
# from authlib.integrations.flask_client import OAuth


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

@api.route("/login", methods=['POST'])
def log_in():
    err_description = ""
    try:
        body = request.get_json()
        username = body.get("username", None)
        password = body.get("password", None)
        
        if username is None or password is None: 
            abort(401)

        usuario =  Usuario.query.filter_by(username = username).first()

        if  usuario is not None and \
            usuario.check_password(password):
            print(f"user -> {usuario}")
            print(usuario.get_attributes())
            print(type(usuario.get_attributes()))
            login_user(usuario, remember=True)
            return jsonify({
                'success': True,
                'code': 200,
                'endpoint': '/log-in',
                'method': 'POST',
                'user': usuario.get_attributes()
            })    
        else: 
            if usuario is None:
                err_description = "user not found"
            elif not usuario.check_password(password):
                err_description = "incorrect password"
    except Exception as e:
        print(f"EXCEPTION: {e}")
        if err_description == "user not found":
            abort(403, description=err_description)
        else:
            abort(500, description=err_description)


@api.route("/sign-up", methods=['POST'])
def create_user():
    try:
        body = request.get_json()
        print(body)
        username = body.get('username', None)
        email = body.get('email', None)
        password = body.get('password', None)
        print(username)
        print(email)
        print(password)
        print(body.get('send',None))
        if username is None or email is None or password is None:
            abort(422)
        
        usuario =  Usuario.query.filter_by(email = email).one_or_none()
        if usuario is not None:
            abort(422)
        
        usuario = Usuario.query.filter_by(username = username).one_or_none()
        if usuario is not None:
            abort(422)

        new_user =  Usuario(email, 
                            username, 
                            password)
        new_user_id = new_user.insert()
        
        login_user(new_user)

        return jsonify({
            'success': True,
            'code': 200,
            'endpoint': '/sign-up',
            'method': 'POST',
            'created': new_user_id,
        })
    except Exception as e:
        print(f"EXCEPTION: {e}")
        abort(500)

@api.route("/user/<user_id>", methods=['DELETE'])
def delete_user_by_id(user_id):
    error_404 = False
    try:
        user = Usuario.query.filter(Usuario.email == user_id).one_or_none()

        if user is None:
            error_404 = True
            abort(404)
        user.delete()

        return jsonify({
            'success': True,
            'code': 200,
            'deleted': user_id
            })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)

@api.route("/logout", methods=['GET', 'POST'])
#@login_required
def logout():
    logout_user()
    
    return jsonify({
        'success': True,
        'code': 200,
        'endpoint': '/logout'                                    
        }) 

@api.route('/editar-perfil/', methods=['PATCH'])
@login_required
def update_perfil():
    error_404 = False
    try: 
        userInfo= Usuario.query.filter_by(username=current_user.username).one_or_none()
        
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
                'code': 200,
                'success': True,
                'endpoint': '/editar-perfil',
                'method': 'PATCH',
                'id': current_user.email
            })

    except:
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/posts', methods=['GET'])
@login_required
def get_posts():

    selection = Post.query.order_by('id').all()
    posts = paginate_items(request, selection)

    if len(posts) == 0:
        abort(404)
    #deberia ser abort? o mas bien enviar lista vacia y que el 
    #front muestre todo vacio?
    
    return jsonify({
        'success': True,
        'code': 200,
        'endpoint': '/posts',
        'method': 'GET',
        'posts': posts,
        'total_posts': len(selection)
    })

@api.route("/posts", methods=['POST'])
#@login_required
def create_post():

    body = request.get_json()

    titulo = body.get('titulo', None)
    subtitulo = body.get('subtitulo', None)
    contenido = body.get('contenido', None)
    portada = body.get('portada', None)
    id_autor = body.get('teacher_email', None)
    search = body.get('search', None)

    if search:
        selection = Post.query.order_by('id').filter(Post.titulo.like('%{}%'.format(search))).all()
        posts = paginate_items(request, selection)
        return jsonify({
            'code': 200,
            'success': True,
            'endpoint': '/posts',
            'method': 'POST',
            'posts': posts,
            'total_posts': len(selection)
        })

    if titulo is None or subtitulo is None or contenido is None:
        abort(422)

    #if portada is None: set portada a imagen por default/vacio

    try:
        img = portada
        #filename = secure_filename(img)
        #print(img.filename)

        #casi seguro que el path cambia con una carpeta del front
        #img.save(os.path.join('app/static/img/portada/', filename))

        realname = img.replace(' ', '_')

        if id_autor == None:
            post = Post(
                id=hashlib.md5(titulo.encode()).hexdigest(),
                titulo=titulo,
                subtitulo=subtitulo,
                id_autor=current_user.email,
                fecha=datetime.now(),
                contenido=contenido,
                portada = portada        
            )
        elif id_autor:
            post = Post(
                id=hashlib.md5(titulo.encode()).hexdigest(),
                titulo=titulo,
                subtitulo=subtitulo,
                id_autor=id_autor,
                fecha=datetime.now(),
                contenido=contenido,
                portada = portada        
            )

        new_post_id = post.insert()

        selection = Post.query.order_by('id').all()
        current_posts = paginate_items(request, selection)

        return jsonify({
            'success': True,
            'code': 200,
            'endpoint': '/posts',
            'method': 'POST',
            'created': new_post_id,
            'posts' : current_posts,
            'total_todos' : len(selection)
        })
    except Exception as e:
        print(e)
        abort(500)


@api.route("/posts/<post_id>", methods=['PATCH'])
@login_required
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
        #se rehashearia el id pq el titulo cambio?
        #algun update de fecha?
        #algun update de portada?

        return jsonify({
            'code': 200,
            'success': True,
            'endpoint': '/posts',
            'method': 'PATCH',
            'updated_id': post_id
        })
    except:
        if error_404:
            abort(404)
        else:
            abort(500)

@api.route('/posts/<post_id>', methods=['DELETE'])
@login_required
def delete_posts_by_id(post_id):
        error_404 = False
        try:
            post = Post.query.filter(Post.id == post_id).one_or_none()
            if post is None:
                error_404 = True
                abort(404)

            post.delete()

            selection = Post.query.order_by('id').all()
            posts = paginate_items(request, selection)

            return jsonify({
                'code': 200,
                'success': True,
                'endpoint': '/posts',
                'method': 'DELETE',
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
@login_required
def get_cursos():

    selection = Curso.query.order_by('id').all()
    cursos = paginate_items(request, selection)

    if len(cursos) == 0:
        abort(404)

    return jsonify({
        'code': 200,
        'success': True,
        'endpoint': '/cursos',
        'method': 'GET',
        'cursos': cursos,
        'total_cursos': len(selection)
    })

@api.route('/cursos', methods=['POST'])
@login_required
def create_cursos():
    body = request.get_json()

    contenido = body.get('contenido',None)
    fecha = datetime.now()
    titulo = body.get('titulo',None)
    subtitulo = body.get('subtitulo',None)
    portada = body.get('photo',None)    
    search = body.get('search',None)

    #creo que falta mejorar el parseado de la portada de acuerdo al forms

    #solo sera search por curso nombre?
    #o por teacher nombre tmb?
    if search:
        selection = Curso.query.order_by('id').filter(Curso.titulo.like('%{}%'.format(search))).all()
        cursos = paginate_items(request, selection)
        return jsonify({
            'code': 200,
            'success': True,
            'endpoint': '/cursos',
            'method': 'POST',
            'cursos': cursos,
            'total_cursos': len(selection)
        })

    if contenido is None or titulo is None or subtitulo is None or portada is None:
        abort(422)
        
    #if portada is None, setear a imagen default

    try:
        id_ = hashlib.md5(titulo.encode()).hexdigest()
        curso = Curso(
            id=id_,
            id_teacher = current_user.email,
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
            'code': 200,
            'success': True,
            'endpoint': '/cursos',
            'method': 'POST',
            'created': new_curso_id,
            'cursos': cursos,
            'total_cursos': len(selection)
        })

    except Exception as e:
        print(e)
        abort(500)

@api.route("/cursos/<curso_id>", methods=['PATCH'])
@login_required
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
        #algun update de portada?

        return jsonify({
                'code': 200,
                'success': True,
                'endpoint': '/cursos',
                'method': 'PATCH',
                'updated_id': curso_id
            })
    except:
            if error_404:
                abort(404)
            else:
                abort(500)

@api.route('/cursos/<curso_id>', methods=['DELETE'])
@login_required
def delete_cursos_by_id(curso_id):
    # DONE
    error_404 = False
    try:
        curso = Curso.query.filter(Curso.id == curso_id).one_or_none()
        if curso is None:
            error_404 = True
            abort(404)

        curso.delete()

        selection = Curso.query.order_by('id').all()
        cursos = paginate_items(request, selection)

        return jsonify({
            'code': 200,
            'success': True,
            'endpoint': '/cursos',
            'method': 'DELETE',
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
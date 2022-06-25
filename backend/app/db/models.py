from email.policy import default
from .database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    # main data
    email = db.Column(db.String(50), primary_key = True)
    username = db.Column(db.String(30), unique=True)
    password_hashed = db.Column(db.String(128), nullable=False)
    
    # personal data
    country = db.Column(db.String(), nullable=True)
    institute = db.Column(db.String(), nullable=True)
    career = db.Column(db.String(), nullable=True)

    # social media
    website = db.Column(db.String(), nullable=True)
    github = db.Column(db.String(), nullable=True)
    twitter = db.Column(db.String(), nullable=True)
    instagram = db.Column(db.String(), nullable=True)
    facebook = db.Column(db.String(), nullable=True)

    confirmacion = db.Column(db.Boolean, default=False)
    confirmacion_date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    photo = db.Column(db.String(), nullable = True, default='profile.jpg')

    #relaciones
    #posts = db.relationship('Post', backref='autor')
    #cursos_lleva = db.relationship('Lleva', backref='lleva')
    #cursos_teach = db.relationship('Curso', backref='teacher')

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hashed = generate_password_hash(password)
        
    
    @property
    def password(self):
        raise AttributeError('Password is not readable')

    def check_password(self,password):
        return check_password_hash(self.password_hashed, password)
    
    def get_id(self):
        return (self.email)

    def __repr__(self) -> str:
        return f'e: {self.email} \tu: {self.username} \tg: {self.github}'

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.String(), primary_key=True)
    id_teacher = db.Column(db.String(50), db.ForeignKey('usuario.email'), nullable=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime(), nullable=True)
    titulo = db.Column(db.String(), nullable=True)    
    subtitulo = db.Column(db.String(), nullable=True)
    portada = db.Column(db.String(), nullable= True)
    #relaciones
    teacher = db.relationship("Usuario", backref="cursos")

class Lleva(db.Model):
    __tablename__ = 'lleva'
    id_curso = db.Column(db.String(), db.ForeignKey('curso.id'), primary_key=True)
    id_user = db.Column(db.String(50), db.ForeignKey('usuario.email'), primary_key = True)

    #relaciones
    student = db.relationship("Usuario", backref="lleva")
    curso = db.relationship("Curso", backref="lleva")

class Post(db.Model):
    __tablename__ = 'post' 
    id = db.Column(db.String(), primary_key=True)
    titulo = db.Column(db.String(), nullable=True)
    subtitulo = db.Column(db.String(), nullable=True)
    id_autor = db.Column(db.String(50), db.ForeignKey('usuario.email'), nullable=True) #cambiar los que hace nreferenca a autor por id_autor
    fecha = db.Column(db.DateTime(), nullable=True)
    contenido = db.Column(db.Text(), nullable=True)
    portada = db.Column(db.String(), nullable= True)

    #relaciones
    autor = db.relationship("Usuario", backref="posts")
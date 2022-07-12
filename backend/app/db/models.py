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
    #0 - student, 1 - teacher, 2 - admin
    tipo_usuario = db.Column(db.Integer, nullable=False, default=0)
    #otra opcion es
    #profesor = db.Column(db.Boolean, default=False)

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

    photo = db.Column(db.String(), nullable = True, default='profile.jpg')
    #qr_yape = db.Column(db.String(), nullable = True)

    #relaciones
    posts = db.relationship('Post', backref='autor', lazy=True)
    cursos_lleva = db.relationship('Lleva', backref='lleva', lazy=True)
    cursos_dicta = db.relationship('Curso', backref='dicta', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hashed = generate_password_hash(password)
        
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.email
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    @property
    def password(self):
        raise AttributeError('Password is not readable')

    def check_password(self,password):
        return check_password_hash(self.password_hashed, password)
    
    def get_id(self):
        return (self.email)

    def get_attributes(self):
        dict_obj = {
            "email" : self.email,
            "username" : self.username,
            "country" : self.country,
            "institute" : self.institute,
            "career" : self.career,
            "website" : self.website,
            "github" : self.github,
            "twitter" : self.twitter,
            "instagram" : self.instagram,
            "facebook" : self.facebook,
            "photo" : self.photo,
        }
        for k, v in dict_obj.items():
            if dict_obj[k] is None:
                dict_obj[k] = ""

        return dict_obj

    def __repr__(self) -> str:
        return f'e: {self.email} \tu: {self.username}'

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.String(), primary_key=True)
    id_teacher = db.Column(db.String(50), db.ForeignKey('usuario.email'), nullable=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime(), nullable=True)
    titulo = db.Column(db.String(), nullable=True)    
    subtitulo = db.Column(db.String(), nullable=True)
    portada = db.Column(db.String(), nullable= True)

    def get_attributes(self):
        return {
            "id": self.id,
            "id_teacher": self.id_teacher,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "subtitulo": self.subtitulo,
            "fecha": self.fecha,
            "portada": self.portada
        }
    
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def update(self):
        try:
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()


class Lleva(db.Model):
    __tablename__ = 'lleva'
    id_curso = db.Column(db.String(), db.ForeignKey('curso.id'), primary_key=True)
    id_user = db.Column(db.String(50), db.ForeignKey('usuario.email'), primary_key = True)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()


    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    #relaciones, me parece que no lleva por ser tabla intermedia 

class Post(db.Model):
    __tablename__ = 'post' 
    id = db.Column(db.String(), primary_key=True)
    titulo = db.Column(db.String(), nullable=True)
    subtitulo = db.Column(db.String(), nullable=True)
    id_autor = db.Column(db.String(50), db.ForeignKey('usuario.email'), nullable=True) #cambiar los que hace nreferenca a autor por id_autor
    fecha = db.Column(db.DateTime(), nullable=True)
    contenido = db.Column(db.Text(), nullable=True)
    portada = db.Column(db.String(), nullable= True)

    def get_attributes(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "subtitulo": self.subtitulo,
            "id_autor": self.id_autor,
            "fecha": self.fecha,
            "contenido": self.contenido,
            "portada": self.portada
        }
        
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def update(self):
        try:
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

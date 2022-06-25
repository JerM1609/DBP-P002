from flask import Blueprint, render_template, request, session
from flask_wtf import FlaskForm
from wtforms import (
    TextAreaField,
    StringField,
    PasswordField,
    validators,
    FileField,
    Form,
    SubmitField
)

from app.db.models import Post

class LoginF(Form):
    username = StringField(
                'Username',
                [validators.DataRequired(message = 'Espacio requerido'),
                 validators.length(min = 5, max = 30, message='No es valido')
                ])
    password =  PasswordField(
                 'Password',
                 [validators.DataRequired(message = 'Espacio requerido')]
                )
    
    def __init__(self, *args, **kwargs):
        super(LoginF, self).__init__(*args, **kwargs)

class SignUpF(Form):
    username = StringField(
                'Username',
                [validators.DataRequired(message = 'Espacio requerido'),
                 validators.length(min = 5, max = 30, message='No es valido')
                ])
    email = StringField(
                        'Email',
                        [validators.DataRequired(message= 'Debes colocar un correo')]
                        )
    password =  PasswordField(
                 'Password',
                 [validators.DataRequired(message = 'Espacio requerido')]
                )
              
    def __init__(self, *args, **kwargs):
        super(SignUpF, self).__init__(*args, **kwargs)

class PostF(FlaskForm):    
    titulo = StringField('Título', [validators.DataRequired(message='Espacio requerido')])
    subtitulo = StringField('Subtítulo', [validators.DataRequired(message='Espacio requerido')])
    clase = StringField('Clase', [validators.DataRequired(message='Espacio requerido')])
    contenido = TextAreaField('Contenido', [validators.DataRequired(message='Espacio requerido')])
    photo = FileField('Portada')
    submit = SubmitField('Submit', [validators.DataRequired(message='Espacio requerido')])
    def __init__(self, *args, **kwargs):
        super(PostF, self).__init__(*args, **kwargs)

#FlaskForm ayuda a que se guarde la data ya cargada
class PerfilEdit(FlaskForm):
    carrera = StringField('¿Cuál es tu carrera?')
    pais = StringField('¿De qué país eres?')
    universidad = StringField('¿A qué universidad perteneces?')
    website = StringField('Website')
    github = StringField('Github')
    twitter = StringField('Twitter')
    ig = StringField('Instagram')
    fb = StringField('Facebook')
    photo = FileField('Foto')
    def __init__(self, *args, **kwargs):
        super(PerfilEdit, self).__init__(*args, **kwargs)

class CrearCurso(FlaskForm):
    titulo = StringField('Título', [validators.DataRequired(message='Espacio requerido')])
    subtitulo = StringField('Subtítulo', [validators.DataRequired(message='Espacio requerido')])
    contenido = TextAreaField('Contenido', [validators.DataRequired(message='Espacio requerido')])
    photo = FileField('Portada')
    submit = SubmitField('Submit', [validators.DataRequired(message='Espacio requerido')])

    def __init__(self, *args, **kwargs):
        super(CrearCurso, self).__init__(*args, **kwargs)
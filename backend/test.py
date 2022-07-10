import unittest
from flask_sqlalchemy import SQLAlchemy
from setuptools import setup
import os
import json
from dotenv import load_dotenv

load_dotenv()

from app import create_app
from app.db.database import setup_db

class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = os.getenv("DB_NAME")
        self.database_path = os.getenv("PSQL_URI") + self.database_name

        setup_db(self.app, self.database_path)
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.usuario = {
            'email' : 'daniel.alpd1001@gmail.com',
            'password' : 'megustadbp',
            'username' : 'MD1001'
        }
        self.editar = {
            'email' : 'daniel.alpd1001@gmail.com',
            'country' : 'Peru',
            'institute' : 'UTEC',
            'career' : 'CS'            
        }
        self.cursos = {            
            'contenido': 'Aprenderemos a utilizar la indexacion de la libreria Faiss',
            'titulo': 'Indexacion de Faiss',
            'subtitulo' : 'Indexando con HNSW',
            'portada' : 'FB_faiss.png',
            'teacher_email' : 'daniel.alpd1001@gmail.com'
        }


        self.posts = {            
            'contenido': 'Aprenderemos a utilizar la indexacion de la libreria Faiss',
            'titulo': 'Indexacion de Faiss',
            'subtitulo' : 'Indexando con HNSW',
            'portada' : 'FB_faiss.png',
            'teacher_email' : 'daniel.alpd1001@gmail.com'
        }



#------------- Usuarios -------------------#
    def test_get_usuarios_success(self):
        res = self.client().post('/user', json = self.usuario)
        data0 = json.loads(res.data)
        
        res = self.client().get('/user')
        data =  json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['users']))

        # Falta eliminar  self.client().delete('/')
    
    
    
    def test_create_usuario(self):
        res = self.client().post('/user', json = self.usuario)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['users']))
        
        # Falta eliminar 

    def test_update_usuario(self):
        res = self.client().post('/user', json = self.usuario)
        data = json.loads(res.data)
        id =  data['created']

        res = self.client().patch('/editar-perfil/', json = self.editar)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['email'], id)
        # Falta eliminar


    

#--------------  Cursos -----------------#


    def test_get_cursos(self): 
        res = self.client().post('/user', json = self.usuario)
        data = json.loads(res.data)
        id_us = data['created']
        res  = self.client().post('/cursos', json = self.cursos)
        data = json.loads(res.data)
        id_curs = data['created']

        res =  self.client().get('/cursos')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['cursos']))
        self.assertTrue(data['total_cursos'])
        
        self.client().delete('/cursos/'+str(id_curs))
        self.client().delete('/user/'+str(id_us))


    
    def test_create_curso(self): 
        res = self.client().post('/user', json = self.usuario)
        data = json.loads(res.data)
        id_us = data['created']
        res  = self.client().post('/cursos', json = self.cursos)
        data = json.loads(res.data)
        id_curs = data['created']

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['cursos']))
        self.assertTrue(data['total_cursos'])


        self.client().delete('/cursos/'+str(id_curs))
        self.client().delete('/user/'+str(id_us))

    
        

#--------------  Posts -----------------#
    def test_get_cursos(self): 
        res = self.client().post('/user', json = self.usuario)
        data = json.loads(res.data)

        res  = self.client().post('/cursos', json = self.cursos)

        res =  self.client().get('/cursos')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['cursos']))
        self.assertTrue(data['total_cursos'])

        
    def test_create_posts(self): 
        res = self.client().post('/user', json = self.usuario)
        data = json.loads(res.data)
        id_us = data['created']
        res  = self.client().post('/posts', json = self.cursos)
        data = json.loads(res.data)
        id_curs = data['created']

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['cursos']))
        self.assertTrue(data['total_cursos'])


        self.client().delete('/cursos/'+str(id_curs))
        self.client().delete('/user/'+str(id_us))


    def tearDown(self):
        pass

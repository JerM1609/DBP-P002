import unittest
from flask_jwt_extended import create_access_token
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
        self.database_path = 'postgresql://postgres:72869881@localhost:5432/dbpv2' 

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
    """
    def test_get_usuarios_success(self):
        res = self.client().post('/user', json = self.usuario)
        data0 = json.loads(res.data)
        
        res = self.client().get('/user')
        data =  json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['users']))

        # Falta eliminar  self.client().delete('/')
    """
    
    
    def test_create_usuario(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        token = data['access_token']
        headers={
            "Authorization":f"Bearer {token}"
        }
        res = self.client().delete('/user', headers=headers)
        data = json.loads(res.data)        
        
        res = self.client().post('/logout')
        data = json.loads(res.data)        
        

        """
        res = self.client().post('/log-in', json = self.usuario)
        data = json.loads(res.data)        
        print(data)
        token = data['access_token']
        headers={
            "Authorization":f"Bearer {token}"
        }
        res = self.client().get('/posts',headers=headers)
        data = json.loads(res.data)        
        print(data)
        """    

        
    
    def test_update_usuario(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        #print(data)
        
        token = data['access_token']
        headers={
            "Authorization":f"Bearer {token}"
        }

        res  = self.client().patch('/editar-perfil/', headers=headers, json=self.editar)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        res = self.client().delete('/user', headers=headers)
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)        
        
        # Falta eliminar

    def test_delete_usuario(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        #print(data)
        
        token = data['access_token']
        headers={
            "Authorization":f"Bearer {token}"
        }        
        
        res = self.client().delete('/user', headers=headers)
        data = json.loads(res.data)        
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], self.usuario['email'])


        res = self.client().post('/logout')
        data = json.loads(res.data)     


    

#--------------  Cursos -----------------#


    def test_get_cursos(self): 
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        
        
        token = data['access_token']
        headers={
            "Authorization":f"Bearer {token}"
        }        

        
        res  = self.client().post('/creation_cursos', headers=headers, json = self.cursos)
        data = json.loads(res.data)
        id_post = data['created']

        res  = self.client().get('/cursos', headers=headers)
        data = json.loads(res.data)

        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['cursos']))
        self.assertTrue(data['total_cursos'])
        
        res = self.client().delete('/cursos/'+str(id_post), headers=headers)

        res = self.client().delete('/user', headers=headers)
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)    




    def test_create_curso(self): 
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        
        
        token = data['access_token']
        headers={
            "Authorization":f"Bearer {token}"
        }        

        
        res  = self.client().post('/creation_cursos', headers=headers, json = self.cursos)
        data = json.loads(res.data)
        id_post = data['created']

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['cursos']))
        self.assertTrue(data['total_cursos'])        
        
        
        
        res = self.client().delete('/cursos/'+str(id_post), headers=headers)

        res = self.client().delete('/user', headers=headers)
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)    
    
        

#--------------  Posts -----------------#
    def test_get_posts(self): 
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        
        
        token = data['access_token']
        headers={
            "Authorization":f"Bearer {token}"
        }        

        
        res  = self.client().post('/creation_posts', headers=headers, json = self.posts)
        data = json.loads(res.data)
        id_post = data['created']

        res  = self.client().get('/posts', headers=headers)
        data = json.loads(res.data)

        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['posts']))
        self.assertTrue(data['total_posts'])
        
        res = self.client().delete('/posts/'+str(id_post), headers=headers)

        res = self.client().delete('/user', headers=headers)
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)     

    
    def test_create_posts(self): 
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        
        
        token = data['access_token']
        headers={
            "Authorization":f"Bearer {token}"
        }        

        
        res  = self.client().post('/creation_posts', headers=headers, json = self.posts)
        data = json.loads(res.data)
        id_post = data['created']
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['posts']))
        self.assertTrue(data['total_posts'])
        
        res = self.client().delete('/posts/'+str(id_post), headers=headers)

        res = self.client().delete('/user', headers=headers)
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)     



    def tearDown(self):
        pass

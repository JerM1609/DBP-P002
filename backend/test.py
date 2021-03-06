from ctypes import c_int
import unittest
from flask_jwt_extended import create_access_token
from flask_sqlalchemy import SQLAlchemy
from requests import head

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
        self.database_path = 'postgresql://postgres:1234@localhost:5432/dbp20_test' 

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
        self.login_usuario = {
            'email' : 'daniel.alpd1001@gmail.com',
            'password' : 'megustadbp'            
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
        self.cursos_edit = {            
            'contenido': 'Aprenderemos a utilizar la indexacion de la libreria Faiss',
            'titulo': 'Indexacion de Faiss',
            'subtitulo' : 'Indexando con HNSW',
            'portada' : 'FB_faiss.png'         
        }

        self.posts = {            
            'contenido': 'Aprenderemos a utilizar la indexacion de la libreria Faiss',
            'titulo': 'Indexacion de Faiss',
            'subtitulo' : 'Indexando con HNSW',
            'portada' : 'FB_faiss.png'            
        }
        self.posts_edit = {            
            'contenido': 'Aprenderemos a utilizar la indexacion de la libreria Faiss',
            'titulo': 'Indexacion de Faiss',
            'subtitulo' : 'Indexando con HNSW',
            'portada' : 'FB_faiss.png'            
        }



#------------- Usuarios -------------------#
    
    
    def test_create_usuario(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        user_id = data['created']

        self.assertEqual(res.status_code, 200)        

        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

        res = self.client().delete('/user/'+str(user_id) )
        data = json.loads(res.data)        
        
        res = self.client().post('/logout')
        data = json.loads(res.data)        
    def test_log_in(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']
        res = self.client().post('/log-in', json = self.login_usuario)
        data = json.loads(res.data)                
        
       
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['user_id'], c_user)

        res = self.client().delete('/user/'+str(c_user))
        data = json.loads(res.data)        
        
        res = self.client().post('/logout')
        data = json.loads(res.data)      
    
    def test_log_in_failed(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']
                
        res = self.client().post('/log-in', json = {})
        data = json.loads(res.data)                


        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], 'Unauthorized')
        self.assertEqual(data['success'], False)

        res = self.client().delete('/user/'+str(c_user))
        data = json.loads(res.data)        
        
        res = self.client().post('/logout')
        data = json.loads(res.data)      


    
    def test_create_usuario_fail(self):
        res = self.client().post('/sign-up', json = {})
        data = json.loads(res.data)        
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        
        
    def test_update_usuario(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']


        res  = self.client().patch('/editar-perfil/', json=self.editar)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        res = self.client().delete('/user/'+str(c_user))
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)        
        
    

    def test_delete_usuario(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']
        
        res = self.client().delete('/user/'+str(c_user))
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
        c_user = data['created']
    

        
        res  = self.client().post('/creation_cursos',  json = self.cursos)
        data = json.loads(res.data)
        id_post = data['created']

        res  = self.client().get('/cursos', json= {'email': c_user})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['cursos']))
        self.assertTrue(data['total_cursos'])
        
        res = self.client().delete('/cursos/'+str(id_post) )

        res = self.client().delete('/user/'+str(c_user) )
        res = self.client().post('/logout')

            
    def test_delete_cursos(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user= data['created']
       
        res  = self.client().post('/creation_cursos', json = self.cursos)
        data = json.loads(res.data)
        id_post = data['created']

        res = self.client().delete('/cursos/'+str(id_post))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], id_post)

        res = self.client().delete('/user/'+str(c_user) )        

    
        res = self.client().post('/logout')
        data = json.loads(res.data)     

    def test_delete_cursos_failed(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']
        

        res = self.client().delete('/cursos/-10' )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)           
        self.assertEqual(data['message'], 'resource not found')

        res = self.client().delete('/user/'+str(c_user))
        res = self.client().post('/logout')
    

    def test_update_cursos(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        
        c_user = data['created']  

        res  = self.client().post('/creation_cursos', json = self.posts)
        data = json.loads(res.data)
        id_post = data['created']

        res = self.client().patch('/cursos/'+str(id_post), json = self.posts_edit)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated_id'], id_post)

        res = self.client().delete('/cursos/'+str(id_post))


        res = self.client().delete('/user/'+str(c_user))
        res = self.client().post('/logout')

    
    def test_update_cursos_failed(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']
        

        res  = self.client().post('/creation_cursos', json = self.posts)
        data = json.loads(res.data)
        id_post = data['created']


        res = self.client().patch('/cursos/-10',json=self.cursos_edit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        
        res = self.client().delete('/cursos/'+str(id_post))

        res = self.client().delete('/user/'+str(c_user))
        res = self.client().post('/logout')
    


    def test_create_curso(self): 
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']
        
                

        
        res  = self.client().post('/creation_cursos', json = self.cursos)
        data = json.loads(res.data)
        id_post = data['created']

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['cursos']))
        self.assertTrue(data['total_cursos'])        
        
        
        
        res = self.client().delete('/cursos/'+str(id_post))

        res = self.client().delete('/user/'+str(c_user))
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)   

    
    def test_create_curso_fail(self): 
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user= data['created']
        
    
        
        res  = self.client().post('/creation_cursos',  json = {})
        data = json.loads(res.data)

        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')        
        
                

        res = self.client().delete('/user/'+str(c_user) )
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)    
        

#--------------  Posts -----------------#
    def test_get_posts(self): 
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']
        
        
        
        res  = self.client().post('/creation_posts', json = self.posts)
        data = json.loads(res.data)
        id_post = data['created']

        res  = self.client().get('/posts', json={'email': c_user})
        data = json.loads(res.data)

        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['posts']))
        self.assertTrue(data['total_posts'])
        
        res = self.client().delete('/posts/'+str(id_post))

        res = self.client().delete('/user/'+str(c_user))
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)    

    def test_delete_posts(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']

        res  = self.client().post('/creation_posts', json = self.posts)
        data = json.loads(res.data)
        id_post = data['created']

        res = self.client().delete('/posts/'+str(id_post))

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], id_post)

        res = self.client().delete('/user/'+str(c_user))
        res = self.client().post('/logout')

    

    def test_delete_posts_failed(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        
        c_user = data['created']

        res = self.client().delete('/posts/-10' )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)           
        self.assertEqual(data['message'], 'resource not found')

        res = self.client().delete('/user/'+str(c_user))
        res = self.client().post('/logout')




    def test_update_posts(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']
        res  = self.client().post('/creation_posts', json = self.posts)
        data = json.loads(res.data)
        id_post = data['created']

        res = self.client().patch('/posts/'+str(id_post), json = self.posts_edit)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated_id'], id_post)

        res = self.client().delete('/posts/'+str(id_post))


        res = self.client().delete('/user/'+str(c_user))
        res = self.client().post('/logout')


    def test_update_posts_failed(self):
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']                

        res  = self.client().post('/creation_posts', json = self.posts)
        data = json.loads(res.data)
        id_post = data['created']


        res = self.client().patch('/posts/-10',json=self.posts_edit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        
        res = self.client().delete('/posts/'+str(id_post))

        res = self.client().delete('/user/'+str(c_user))
        res = self.client().post('/logout')



    def test_create_posts(self): 
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']            
        
        
        res  = self.client().post('/creation_posts', json = self.posts)
        data = json.loads(res.data)
        id_post = data['created']
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['posts']))
        self.assertTrue(data['total_posts'])
        
        res = self.client().delete('/posts/'+str(id_post))

        res = self.client().delete('/user/'+str(c_user))
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data)     

    def test_create_posts_fail(self): 
        res = self.client().post('/sign-up', json = self.usuario)
        data = json.loads(res.data)        
        c_user = data['created']           


        
        res  = self.client().post('/creation_posts', json = {})
        data = json.loads(res.data)

        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')        
                    

        res = self.client().delete('/user/'+str(c_user))
        data = json.loads(res.data)        
        res = self.client().post('/logout')
        data = json.loads(res.data) 
    """                    
    """
    def tearDown(self):
        pass

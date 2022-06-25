import unittest
from flask_sqlalchemy import SQLAlchemy
from setuptools import setup
import os
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
    
    def tearDown(self):
        pass
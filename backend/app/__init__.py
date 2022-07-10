from flask import Flask, render_template
from flask_login import LoginManager
from flask_cors import CORS
from .db.database import db, migrate
from .config.config import Config
from .endpoints import configure_mails, init_login, api as API
from .db.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app, origins=['https://utec.edu.pe', 'http://127.0.0.1:5001', 'http://127.0.0.1:8080'], max_age=10)
    # CORS(app, resources={r'/*':{'origins': 'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})
    # app.config['CORS_HEADERS'] = 'Content-Type'
    db.init_app(app)    

    with app.app_context():
        db.create_all()
    
    migrate.init_app(app, db)        

    app.register_blueprint(API)
    init_login(app)
    configure_mails(app)

    print(app.config['UPLOAD_FOLDER'])


    @app.after_request
    def after_resquest(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,PUT,OPTIONS')
        return response
        
    return app

"""
https://stackoverflow.com/questions/46540664/no-application-found-either-work-inside-a-view-function-or-push-an-application
"""
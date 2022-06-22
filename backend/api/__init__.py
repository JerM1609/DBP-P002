from flask import Flask, render_template
from flask_login import LoginManager
from flask_cors import CORS
from .db.database import db, migrate
from .config.config import Config
from .endpoints import configure_mails, api as API, init_login
from .db.database import db

app = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r'/*':{'origins': 'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})

    db.init_app(app)

    # with app.app_context():
    #     db.create_all()
    
    # register blueprint apps
    app.register_blueprint(API)

    migrate.init_app(app, db)        # Flask DB Migration
    init_login(app)
    configure_mails(app)
    
    print(app.config['UPLOAD_FOLDER'])

    @app.after_request
    def after_resquest(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,PUT,OPTIONS')
        return response
        
    return app

"""
https://stackoverflow.com/questions/46540664/no-application-found-either-work-inside-a-view-function-or-push-an-application
"""
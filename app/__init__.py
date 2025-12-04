from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'senha-secreta'

    
    from app.routes.auth import auth
    app.register_blueprint(auth)

    return app

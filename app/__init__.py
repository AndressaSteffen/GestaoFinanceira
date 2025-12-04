from flask import Flask

def create_app():
    app= Flask (__name__)

    app.config ['SECRET_KEY'] = 'dev'


    @app.route("/")
    def index():
        return "Aplicaçao funcionando!"
    return app
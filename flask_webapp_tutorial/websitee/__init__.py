from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "FSFFEFSF33"

    from .views import views
    from .auth import auth
    from .web_hooks import web_hooks

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(web_hooks, url_prefix="/")

    return app

from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['secret key'] = "adfgfhgjhjk"
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    from views import views

    app.register_blueprint(views, url_prefix='/')
    

    return app

from flask import Flask


def create_app():
    #Create app with configuration as following
    app = Flask(__name__, template_folder='templates')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    from views import views

    app.register_blueprint(views, url_prefix='/')
    

    return app

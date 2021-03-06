from flask import Flask
# from flask.ext.bootstrap import Bootstrap

def create_app():
	app = Flask(__name__)
	# bootstrap = Bootstrap(app)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
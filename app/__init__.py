from flask import Flask
from flask_login import LoginManager
from app.db import db
from app.ma import ma
from app.web.models import User
from app.web.routes import web_bp
from app.inventory.api_1_0.resources import inventory_bp
from app.spzWeb.api_1_0.resources import spzweb_bp
from app.spazioStatus.api_1_0.resources import spazio_status_bp
from app.mqStatus.api_1_0.resources import mq_status_bp
from app.txStatus.api_1_0.resources import tx_status_bp

login_manager = LoginManager()

def create_app():
	app = Flask(__name__)

	app.config['SECRET_KEY'] = '-13=t5&imzf&6jelb@qmpng=k_1^n=33#l=e7^h+#m=v*#w(%7'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sql'
	app.config['SQLALCHEMY_BINDS'] = {
		'SpazioStatus': 'sqlite:///SpazioDatabase.sql',
		'MQStatus': 'sqlite:///MQDatabase.sql',
		'TXSeriesStatus': 'sqlite:///TXSeriesDatabase.sql'
	}
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	login_manager.init_app(app)
	login_manager.login_view = "web_bp.login"

	@login_manager.user_loader
	def load_user(id):
		return User.get_by_id(int(id))

	db.init_app(app)
	ma.init_app(app)

	app.url_map.strict_slashes = False

	# Registro de los Blueprints
	app.register_blueprint(inventory_bp)
	app.register_blueprint(web_bp)
	app.register_blueprint(spzweb_bp)
	app.register_blueprint(spazio_status_bp)
	app.register_blueprint(mq_status_bp)
	app.register_blueprint(tx_status_bp)

	return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from flask_procmc import Market
import os
from os.path import abspath, join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
basedir = abspath(dirname(__file__))

app = Flask(__name__)

app.config.from_object('config')
app.secret_key = os.environ.get('SECRET_KEY')
postgres_password = os.environ.get('POSTGRES_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://tkrtxt:{postgres_password}@localhost:5433/tkrtxt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')



# stripe_keys = {
#  'secret_key': os.environ['SECRET_KEY'],
#  'publishable_key': os.environ['PUBLISHABLE_KEY']
# }
#stripe.api_key = stripe_keys['secret_key']


login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message = 'Access Denied.'
login.login_message_category = "warning"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

## PICK PRO or SANDBOX in the .env

if os.environ.get('ENV_SETTING') != "PRODUCTION":
    market_key =  os.environ.get('SANDBOX_MARKET')
    sandbox = True
else:
    market_key =  os.environ.get('PRO_MARKET')
    sandbox = False

market = Market(api_key=market_key, sandbox=sandbox)


# blueprints

from tkrtxt.api import bp as api_bp
from tkrtxt.site import bp as site_bp
from tkrtxt.admin import bp as admin_bp
from tkrtxt.auth import bp as auth_bp


# blueprint registrations

app.register_blueprint(site_bp)
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(auth_bp, url_prefix='/auth')



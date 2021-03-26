import dash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
server.config.from_object(Config)

db = SQLAlchemy(server)
migrate = Migrate(server, db)

app = dash.Dash(__name__,
                server=server,
                external_stylesheets=external_stylesheets
                )
app.config.suppress_callback_exceptions = True
login_manager = LoginManager()
login_manager.init_app(server)



# auth = dash_auth.BasicAuth()


from application.callbacks.init_callback import app
from application.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




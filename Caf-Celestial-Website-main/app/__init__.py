from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#-----#-----#-----#-----#-----#-----#

# create the extension
# create the app
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///celulasdecafe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'feahifheaifhseuifonsaefjneafuihefua'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

#-----#-----#-----#-----#-----#-----#

from app.views import IndexPage # aqui é para mudar dps para HomePage
from app.models import Itens, Usuario
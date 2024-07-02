from flask import Flask

#-----#-----#-----#-----#-----#-----#

app = Flask(__name__)




#-----#-----#-----#-----#-----#-----#

from app.views import IndexPage # aqui é para mudar dps para HomePage
#   from app.views import HomePage 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c9aed5040b7686c8918957a4a3d2b0c6'
# sqlite is a convenient way to set up a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #login is the function name of login route
login_manager.login_message_category = 'danger' 

# be aware of Circulation errors!
from flaskBlog import routes

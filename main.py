from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\User\\Documents\\frontend\\gian_flask\\gian.sqlite3'
app.config['SECRET_KEY'] = 'moredevs'

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)

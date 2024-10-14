from flask import Flask
from database import db
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
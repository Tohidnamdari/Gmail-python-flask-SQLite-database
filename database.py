from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY']='jhvhijghlkbvhjvjkjhvcj'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    def __repr__(self):
        return f'Users({self.name},{self.email},{self.password})'

class send_m(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_mab = db.Column(db.Text)
    email_mag = db.Column(db.Text)
    message = db.Column(db.Text)

    def __repr__(self):
        return f'send_m({self.email_mab},{self.email_mag},{self.message})'


from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from main import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(255))
    cars = db.relationship('Car', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Car(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    make = db.Column(db.String(255), index=True)
    model = db.Column(db.String(255), index=True)
    registry = db.Column(db.String(12), index=True, unique=True)
    year = db.Column(db.Integer, index=True)
    power = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    services = db.relationship('Service', backref='car', lazy=True)

    def __repr__(self):
        return '<Car {} Registry '.format(self.model)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    description = db.Column(db.String(255), index=True)
    price = db.Column(db.Integer, index=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)

    def __repr__(self):
        return 'Service {} cost: {}'.format(self.name, self.price)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

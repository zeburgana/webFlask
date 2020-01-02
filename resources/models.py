from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String)
    cars = db.relationship('Car', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Car(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    make = db.Column(db.String(255), index=True)
    model = db.Column(db.String(255), index=True)
    registry = db.Column(db.String(12), index=True, unique=True)
    year = db.Column(db.Integer(5), index=True)
    power = db.Column(db.Integer(5), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    services = db.relationship('Service', backref='car', lazy=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    description = db.Column(db.String(255), index=True)
    price = db.Column(db.Float(8), index=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
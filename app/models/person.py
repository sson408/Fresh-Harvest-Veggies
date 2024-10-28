from app import db

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    typeId = db.Column(db.Integer)
    phoneNumber = db.Column(db.String(100))
    email = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': 'typeId'
    }
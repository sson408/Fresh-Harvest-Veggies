from app import db
from .person import Person

class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    dateJoined = db.Column(db.Date)
    departmentId = db.Column(db.Integer)
    

    __mapper_args__ = {
        'polymorphic_identity': 'staff'
    }
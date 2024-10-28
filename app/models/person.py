from flask import jsonify
from app import db
from flask_hashing import Hashing

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    roleId = db.Column(db.Integer)
    phoneNumber = db.Column(db.String(100))
    email = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': 'roleId'
    }

    def __init__(self, firstName, lastName, username, password, roleId, phoneNumber, email):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__username = username
        self.__password = password
        self.__roleId = roleId
        self.__phoneNumber = phoneNumber
        self.__email = email


    @classmethod
    def register(cls, userName, password):
        #check if the user exists
        existingUser = cls.query.filter_by(username=userName).first()
        if existingUser:
            return jsonify({'message': 'Username already exists'}), 400
        
        #hash the password
        passwordHash = Hashing.hash_value(password, salt='hash')

        #new user
        newUser = cls(userName, passwordHash)
        

    def __str__(self):
        """
        Returns the string representation of the user.
        """
        return self.__firstName + ' ' + self.__lastName
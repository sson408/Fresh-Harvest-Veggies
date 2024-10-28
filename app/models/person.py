from flask import jsonify, session
from app import db
from .enum import userRole
from flask_hashing import Hashing
from sqlalchemy.exc import SQLAlchemyError
hashing = Hashing()

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
        'polymorphic_identity': 1,
        'polymorphic_on': 'roleId'
    }

    def __init__(self, firstName, lastName, username, password, roleId, phoneNumber, email):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.roleId = roleId
        self.userRole = userRole(roleId).name if roleId else ""
        self.phoneNumber = phoneNumber
        self.email = email


    def toDict(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'username': self.username,
            'roleId': self.roleId,
            'userRole':userRole(self.roleId).name if self.roleId else "",
            'phoneNumber': self.phoneNumber,
            'email': self.email
        }
    @classmethod
    def register(cls, username, password):
        try:
            #check if the user exists
            existingUser = cls.query.filter_by(username=username).first()
            if existingUser:
                return jsonify({'message': 'Username already exists'}), 400
            
            #hash the password
            passwordHash = hashing.hash_value(password, salt='hash')

            #new user
            newUser = cls(
                username = username,
                password = passwordHash,
                roleId = 1,
                firstName = '',
                lastName = '',
                phoneNumber = '',
                email = ''
            )
        
        
            #save data to the database
            db.session.add(newUser)
            db.session.commit()

            userId = newUser.id

            if userId:
                # Set the session variables
                session['loggedin'] = True
                session['userId'] = userId
                session['username'] = username
                session['userRole'] = userRole(1).name

            return jsonify({'message': 'User registered successfully', 'userId': userId}), 200
        
        except Exception as e:
            print(f"An error occurred: {e}")
            db.session.rollback()
            return  jsonify({'message': 'An error occurred while registering'}), 500

    @classmethod
    def login(cls, username, password):
        #check if the user exists
        existingUser = cls.query.filter_by(username=username).first()
        if not existingUser:
            return jsonify({'message': 'User not found'}), 404
        
        #verify password
        if hashing.check_value(existingUser.password, password, salt='hash'):
            # Set the session variables
            session['loggedin'] = True
            session['userId'] = existingUser.id
            session['username'] = username
            session['userRole'] = userRole(existingUser.roleId).name
            return jsonify({'message': 'Login successful', 'user': existingUser.toDict()}), 200
        else:
            return jsonify({'message': 'Invalid password'}), 401
        
    
    def __str__(self):
        """
        Returns the string representation of the user.
        """
        return self.__firstName + ' ' + self.__lastName
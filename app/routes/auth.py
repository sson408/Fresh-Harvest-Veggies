from flask import Blueprint, request, jsonify, session
from app.models.person import Person

# Blueprint for auth routes
auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('userName')
        password = data.get('password')
        response, status_code = Person.register(username, password)
        return response, status_code
    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500


@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        response, status_code = Person.login(username, password)
        return response, status_code
    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500


@auth.route('/logout', methods=['POST'])
def logout():
    # Remove session data
    session.pop('loggedin', None)
    session.pop('userId', None)
    session.pop('username', None)
    session.pop('userRole', None)
    
    return jsonify({'message': 'Logout successful'}), 200
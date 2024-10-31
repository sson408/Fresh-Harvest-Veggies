from flask import Blueprint, request, jsonify
from app.models.person import Person
from app.models.customer import Customer


# Blueprint for auth routes
user = Blueprint('user', __name__)

@user.route('/listAllCustomers', methods=['GET'])
def listAllCustomers():
    try:
        filterWord = request.args.get('filterWord')
        response, status_code = Customer.list(filterWord)
        return response, status_code
    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500



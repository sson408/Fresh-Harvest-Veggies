from flask import Blueprint, request, jsonify
from app.models.item import Item
from app.models.veggie import Veggie
from app.models.packVeggie import PackVeggie
from app.models.unitPriceVeggie import UnitPriceVeggie
from app.models.weightedVeggie import WeightedVeggie
from app.models.premadeBox import PremadeBox

# Blueprint for auth routes
item = Blueprint('item', __name__)

@item.route('/listAllItems', methods=['GET'])
def listAllItems():
    try:
        filterWord = request.args.get('filterWord')
        response, status_code = Item.listAllVeges(filterWord)
        return response, status_code
    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500

#list all premade boxes details
@item.route('/listAllPremadeBoxes', methods=['GET'])
def listAllPremadeBoxes():
    try:
        response, status_code = PremadeBox.listAllPremadeBoxes()
        return response, status_code
    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500
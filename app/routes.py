from flask import Blueprint, render_template
from app import create_app

main = Blueprint('main', __name__)


@main.route('/signIn')
def signIn():
    return render_template('signIn.html')

@main.route('/signUp')
def signUp():
    return render_template('signUp.html')
from flask import render_template
from app import create_app

app = create_app()

@app.route('/signIn')
def index():
    return render_template('signIn.html')

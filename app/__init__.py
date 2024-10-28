import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, 
                template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates'),
                static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static'))
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main
    app.register_blueprint(main)


    from app.models import (Person, Customer, Staff, CorporateCustomer, 
        Payment, CreditCardPayment, DebitCardPayment,
        Item, Veggie, WeightedVeggie, PackVeggie,
        UnitPriceVeggie, Order, OrderLine, PremadeBox)


    return app

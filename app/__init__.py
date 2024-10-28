from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)


    from app.models import Person, Customer, Staff, CorporateCustomer, Payment, CreditCardPayment, DebitCardPayment, Item, Veggie, WeightedVeggie, PackVeggie, UnitPriceVeggie, Order, OrderLine, PremadeBox
    from app import routes

    return app
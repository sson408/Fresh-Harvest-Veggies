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

    from app.routes.view import views
    app.register_blueprint(views)

    from app.routes.auth import auth
    from app.routes.user import user
    from app.routes.item import item
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(item, url_prefix='/item')



    from app.models import (Person, Customer, Staff, CorporateCustomer, 
        Payment, CreditCardPayment, DebitCardPayment,
        Item, Veggie, WeightedVeggie, PackVeggie,
        UnitPriceVeggie, Order, OrderLine, PremadeBox, PremadeBoxItem)


    return app

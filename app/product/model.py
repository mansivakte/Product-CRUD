from app.db import db
import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    imagepath = db.Column(db.String(80))
    created_by = db.Column(db.Integer, default = 0)
    created_date = db.Column(db.DateTime(timezone=True),default=datetime.datetime.utcnow)
    updated_by = db.Column(db.Integer, default = 0)
    updated_date = db.Column(db.DateTime(timezone=True), default=None)
    is_updated =db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
    

    def __init__(self,name,description, quantity, price, imagepath):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.imagepath = imagepath

    def __repr__(self):
        return f'<Product id:{self.id} name:{self.name} description:{self.description} quantity:{self.quantity} price:{self.price} imagepath:{self.imagepath}>'
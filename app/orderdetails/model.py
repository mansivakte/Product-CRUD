import datetime
from app.db import db

class Orderdetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    product_price = db.Column(db.Integer)
    product_qty = db.Column(db.Integer)
    total_price = db.Column(db.Integer)

# order_details
    # order_id >> order table
    # priduct_id >>payload
    # product_price >> Product class
    # product_qty >>>> payload
    #  total price =  product_price * product_qty

def __init__(self, order_id, product_price, product_id,product_qty,total_price):
    self.order_id= order_id
    self.product_id = product_id
    self.product_price = product_price
    self.product_qty = product_qty
    self.total_price = total_price
  

def __repr__(self):
        return f'<Orderdetails id:{self.id} order_id:{self.order_id} product_price:{self.product_price} product_qty:{self.product_qty} total_price:{self.total_price}>'

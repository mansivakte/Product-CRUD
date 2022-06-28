from app.db import db

class Orderdetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # order_id
    # priduct_id
    # product_price 
    # product_qty >>>> payload
    #  total price =  product_price * product_qty
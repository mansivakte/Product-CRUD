import uuid
# UUID: Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids
import datetime
from app.db import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    order_date = db.Column(db.DateTime(timezone=True),default=datetime.datetime.utcnow)
    order_status = db.Column(db.Integer, default = 1)
    amount = db.Column(db.Integer)


def __init__(self, order_id, order_date, order_status,amount):
    self.order_id= order_id
    self.order_date = order_date
    self.order_status = order_status
    self.amount = amount
  

def __repr__(self):
        return f'<Order id:{self.id} order_id:{self.order_id} order_date:{self.order_date} amount:{self.amount}>'

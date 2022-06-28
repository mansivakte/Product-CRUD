import uuid
import datetime
from flask import Blueprint, request
from .model import Order
from app.db import db
from app.product.model import Product
from app.common import loginRequired

order_blueprint = Blueprint('order_blueprint', __name__)

@order_blueprint.route('/order', methods=['POST'])
@loginRequired
def createOrder(userid):
    # print("inside create order")
    payload = request.json
    product = payload['order_details']['product']
    # print(product)
    total = 0
    for i in product:
        # print(i['product_id'])
        prdct = Product.query.filter_by(id=i['product_id']).first()
        # print("product id: ", prdct.price ,i['qty'] )
        # print(prdct)
        total += (prdct.price * i['qty'])
    print("Total: ", total)
    order= Order(amount = total, order_id= str(uuid.uuid1()), order_date=datetime.datetime.now() )
    order.user_id= userid
    # print("order : ", type(uuid.uuid1()))
    db.session.add(order)
    db.session.commit()
    return {"status": "executed"}


    
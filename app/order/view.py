import uuid
import datetime
from app.db import db
from flask import Blueprint, request
from .model import Order
from app.orderdetails.model import Orderdetails
from app.product.model import Product
from app.common import loginRequired

order_blueprint = Blueprint('order_blueprint', __name__)

@order_blueprint.route('/order', methods=['POST'])
@loginRequired
def createOrder(userid):
    #1. create order

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
    
   
    #2. Order details

    for i in product:
        prdct = Product.query.filter_by(id=i['product_id']).first()
        orderdetails = Orderdetails(
            order_id=order.order_id,
            product_id = i['product_id'],
            product_price = prdct.price,
            product_qty = i['qty'],
            total_price = (prdct.price * i['qty'])
        )
        quantity = int(prdct.quantity) - int(i['qty']) 
        prdct.quantity = quantity

        print('orderdetails : ',orderdetails)
        db.session.add(orderdetails)
        db.session.commit()

    #3. remaining quantity = total qty - ordered qty

    # for i in product:
    #     prodct = Product.query.filter_by(id=i['product_id']).first()
        
    #     quantity = int(prodct.quantity) - int(i['qty']) 
    #     prodct.quantity = quantity

        
    #     # db.session.add(product)
    #     db.session.commit()
    return {"status": "executed"}
   

@order_blueprint.route('/order', methods=['GET'])
def getOrder():

    order = Order.query.all()
    odr = []
    for i in order:
        a = {
            'id':i.id,
            'amount':i.amount,
            'order_id':i.order_id,
            'order_date':i.order_date
        }
        odr.append(a)
    return {"data": odr}

@order_blueprint.route('/orderdetails', methods=['GET'])
def getOrderdetails():

    orderdetails = Orderdetails.query.all()
    odr = []
    for i in orderdetails:
        a = {
            'id':i.id,
            'order_id':i.order_id,
            'product_id':i.product_id,
            'product_price':i.product_price,
            'product_qty': i.product_qty,
            'total_price': i.total_price
        }
        
        odr.append(a)
    return {"data": odr}
           
        
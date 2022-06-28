import jwt
from flask import request
from app.user.model import User
from app.product.model import Product
from functools import wraps

def loginRequired(fun):
    @wraps(fun)
    def innerFun(*args, **kwargs):
        try:
            token = request.headers['Authorization']
            decode= jwt.decode(token, "abc", algorithms=["HS256"])
            if decode:
                user = User.query.filter_by(id=decode['id']).first()
                if user:
                    return fun(user.id, *args, **kwargs)
                else:
                    return " 1....Unauthorized user"
            else:
                return " 2....Unauthorized user"
        except Exception as e: 
            print("erroe msg : ", e)
            return " 3....Unauthorized user"
    return innerFun


def adminlogin(func):
    @wraps(func)
    def innerFunc(*args, **kwargs):
        try:
            token = request.headers['Authorization']
            decode= jwt.decode(token, "abc", algorithms=["HS256"])
            if decode:
                user = User.query.filter_by(id=decode['id']).first()
                if user and user.admin:
                    return func(user.id, *args, **kwargs)
                else:
                    return {"message" : '1....Unauthorized admin'}
            else:
                return {"message" : ' 2....Unauthorized admin'}
        except Exception as e: 
            print(e)
            return{"message" : ' 3....Unauthorized admin'}
    return innerFunc

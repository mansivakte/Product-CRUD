import jwt
from flask_bcrypt import generate_password_hash, check_password_hash
from flask import Blueprint, request
from .model import User
from app.db import db
from app.common import loginRequired

user_blueprint = Blueprint('user_blueprint', __name__)

#1. User Registration 
@user_blueprint.route('/register', methods= ['POST'])
def register():
    payload = request.json

    validatorCheck = {}

    if payload['firstName'] == '':
        validatorCheck.update({"firstNameError":"Missing First Name"})
    
    if payload['lastName'] == '':
        validatorCheck.update({"lastNameError":"Missing last Name"})
    
    if payload['email'] == '':
        validatorCheck.update({"emailError":"Missing email id"})

    if payload['password'] == '':
        validatorCheck.update({"passwordError":"Missing password"})

    if validatorCheck == {}:
        user = User.query.filter_by(email = payload['email']).first()
        if user:
            return {'Message': 'Email ID already registered'}, 200
        else:
            user_password = generate_password_hash(payload['password'])
            user = User(email = payload['email'], password = user_password, firstName=payload['firstName'], lastName=payload['lastName'], admin = True)
            db.session.add(user)
            db.session.commit()
            return {'Status':'Registered Successfully'}, 201
    else:
        return {"Message":"Something wents wrong"}


#2. User Login 
@user_blueprint.route('/login', methods = ['POST'])
def login():
    payload = request.json
    user = User.query.filter_by(email= payload['email']).first()
    if user:
        hash_password = check_password_hash(user.password, payload['password'])
        if hash_password:
            jwt_encode = jwt.encode({'id':user.id, 'firstName':user.firstName, 'lastname':user.lastName}, "abc" , algorithm="HS256")
            return {'token': jwt_encode}, 200
        else:
            return {'Message': 'Invalid email/password'},401
    else:
        return {'Message': 'Invalid email/password'},401


#User Dashboard 
@user_blueprint.route('/dashboard', methods=['GET'])
@loginRequired
def dashboard(id):
    
    return "User Dashboard Page"


# #User Order 
# @user_blueprint.route('/userorder', methods=['GET'])
# def order():
#     try:
#         decode = jwt.decode(request.headers['Authorization'], "abc", algorithms=["HS256"])
#         if decode:
#             return {"Message": 'Authorized user of id '+ str(decode['id'])}, 200
#         else:
#             return {"Message": "Unauthorized user"}, 401
#     except:
#         return {"Message": "Unauthorized user"}, 401



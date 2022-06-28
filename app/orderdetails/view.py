from flask import Blueprint, request
from .model import Orderdetails
from app.db import db


orderdetails_blueprint = Blueprint('orderdetails_blueprint', __name__)
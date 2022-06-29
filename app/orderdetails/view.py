import uuid
import datetime
from flask import Blueprint, request
from app.db import db
from app.product.model import Product


orderdetails_blueprint = Blueprint('orderdetails_blueprint', __name__)
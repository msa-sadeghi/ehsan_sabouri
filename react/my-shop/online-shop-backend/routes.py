from flask import Blueprint, jsonify, request
from models import Product


products_routes = Blueprint("products", __name__)


@products_routes.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

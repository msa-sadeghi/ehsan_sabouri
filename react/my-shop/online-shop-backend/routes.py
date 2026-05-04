from flask import Blueprint, jsonify, request
from models import Product
from extensions import db
from utils import error_response

products_routes = Blueprint("products", __name__)


@products_routes.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])


@products_routes.route("/products", methods=["POST"])
def create_product():
    if not request.is_json:
        return error_response("Content-Type must be application/json", 415)
    data = request.json

    required_fields = [
        "name",
        "description",
        "price",
    ]
    for field in required_fields:
        if field not in data:
            return error_response(f"{field} is required")

    if not isinstance(data.get("price"), (int, float)):
        return error_response("price must be a number")

    p = Product(
        name=data["name"],
        description=data["description"],
        price=data["price"],
        image=data.get("image"),
        in_stock=data.get("in_stock", True),
    )

    db.session.add(p)
    db.session.commit()

    return jsonify(p.to_dict()), 201


@products_routes.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    p = Product.query.get_or_404(id)
    return jsonify(p.to_dict())


@products_routes.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    p = Product.query.get_or_404(id)
    data = request.get_json()
    p.description = data.get("description", p.description)
    p.price = data.get("price", p.price)
    p.image = data.get("image", p.image)
    p.name = data.get("name", p.name)
    p.in_stock = data.get("in_stock", p.in_stock)
    db.session.commit()
    return jsonify(p.to_dict())


@products_routes.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    p = Product.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({"message": "Product deleted successfult", "id": id})

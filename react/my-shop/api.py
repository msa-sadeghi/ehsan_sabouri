from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
weatherData = [
    {
        "id": 1,
        "name": "لپ‌تاپ اپل MacBook Pro",
        "price": "35000000",
        "colors": ["نقره ای ", "خاکستری"],
        "inStock": True,
    },
    {
        "id": 2,
        "name": " گوشی سامسونگ Galaxy S24",
        "price": "18000000",
        "colors": ["نقره ای ", "مشکی"],
        "inStock": True,
    },
    {
        "id": 3,
        "name": "تبلت اپل iPad Air",
        "price": "20000000",
        "colors": ["نقره ای ", "مشکی"],
        "inStock": True,
    },
]


@app.route("/")
def home():
    return jsonify(
        {
            "endpoints": ["/all", "city/{city_name}"],
            "message": "your request will be processed",
        }
    )


@app.route("/all")
def get_all_weathers():
    return jsonify(weatherData)


# @app.route("/city/<city_name>")
# def get_city_weather(city_name):
#     city_data = weatherData.get(city_name.lower())
#     if city_data:

#         return jsonify(city_data)
#     return jsonify({"error": "city not found"})


app.run(debug=True, port=5000)

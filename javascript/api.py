from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
weatherData = {
    "tehran": {
        "name": "تهران",
        "temp": 25,
        "description": "آفتابی",
        "humidity": 45,
        "wind": 12,
        "pressure": 1013,
        "feels_like": 23,
        "icon": "☀️",
    },
    "shiraz": {
        "name": "شیراز",
        "temp": 28,
        "description": "صاف",
        "humidity": 35,
        "wind": 8,
        "pressure": 1015,
        "feels_like": 26,
        "icon": "🌤️",
    },
    "isfahan": {
        "name": "اصفهان",
        "temp": 22,
        "description": "ابری",
        "humidity": 50,
        "wind": 15,
        "pressure": 1012,
        "feels_like": 20,
        "icon": "☁️",
    },
    "mashhad": {
        "name": "مشهد",
        "temp": 18,
        "description": "نیمه ابری",
        "humidity": 60,
        "wind": 20,
        "pressure": 1010,
        "feels_like": 16,
        "icon": "⛅",
    },
    "tabriz": {
        "name": "تبریز",
        "temp": 15,
        "description": "بارانی",
        "humidity": 75,
        "wind": 18,
        "pressure": 1008,
        "feels_like": 13,
        "icon": "🌧️",
    },
}


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


@app.route("/city/<city_name>")
def get_city_weather(city_name):
    city_data = weatherData.get(city_name.lower())
    if city_data:

        return jsonify(city_data)
    return jsonify({"error": "city not found"})


app.run(debug=True, port=5000)

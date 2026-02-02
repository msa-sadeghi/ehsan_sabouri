from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
users = [
    {
        "id": 1,
        "name": "ali ahmadi",
        "username": "ali_ahmadi",
        "email": "ali@gmail.com",
        "address": {"city": "tehran"},
        "company": {"name": "tech"},
        "website": "ali-tech.ir",
    },
    {
        "id": 2,
        "name": "maryam karimi",
        "username": "maryam_karimi",
        "email": "maryam@gmail.com",
        "address": {"city": "tehran"},
        "company": {"name": "tech"},
        "website": "mar-tech.ir",
    },
]

posts = [
    {
        "id": 1,
        "title": "post one",
        "content": "content of post one",
        "user_id": 1,
        "body": "this is the body of post one",
    },
    {
        "id": 2,
        "title": "post two",
        "content": "content of post two",
        "user_id": 1,
        "body": "this is the body of post two",
    },
    {
        "id": 3,
        "title": "post three",
        "content": "content of post three",
        "user_id": 2,
        "body": "this is the body of post three",
    },
]


@app.route("/")
def home():
    return jsonify(
        {"endpoints": ["/users", "/posts"], "message": "your request will be processed"}
    )


@app.route("/users")
def get_users():
    return jsonify(users)


app.run(debug=True, port=5000)

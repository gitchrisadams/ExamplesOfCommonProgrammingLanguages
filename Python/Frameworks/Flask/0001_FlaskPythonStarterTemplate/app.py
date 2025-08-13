from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Various types of REST requests


# Basic GET request
# http://localhost:5000
@app.route("/")
def get_root_request():
    return jsonify({"id": 1, "name": "GET root request successful"}), 201


if __name__ == "__main__":
    app.run()

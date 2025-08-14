from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
import os

load_dotenv()

app = Flask(__name__)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bizza.db"
db = SQLAlchemy(app)


# Basic GET request
# http://localhost:5000
@app.route("/")
def get_root_request():
    return jsonify({"id": 1, "name": "GET root request successful"}), 201


# Basic GET request with query params
# GET - http://localhost:5000/query?firstname=chris&lastname=christian
@app.route("/query")
def query_example():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    print(firstname)
    print(lastname)
    if firstname is not None and lastname is not None:
        return jsonify(message="The user's fullname :" + firstname + " " + lastname)
    else:
        return jsonify(message="No query parameters in the url")


# GET request passing variables to end point
# http://localhost:5000/variable/2
@app.route("/variable/<int:variable_id>")
def get_variables(variable_id):
    variable_data = {
        "id": variable_id,
    }
    return jsonify(variable_data)


@app.route("/users")
def get_users():
    users = User.query.all()
    return render_template("users.html", users=users)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique=True)
    name = db.Column(db.String(55), unique=False)
    email = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return "<User {}>".format(self.name)


if __name__ == "__main__":
    app.run()

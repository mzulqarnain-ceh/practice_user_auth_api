from flask import Flask,jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from models import init_db,get_db_connection
from config import SECRET_KEY
from auth import token_required
import jwt
from datetime import datetime,timedelta
# app initialize
app=Flask(__name__)
# Routes
# home route
@app.route("/")
def home():
    return jsonify({"message":"Practice auth api is running"})
# Signup route
@app.route("/signup",methods=["POST"])
def signup():
    pass
# Login route
@app.route("/login",methods=["POST"])
def login():
    pass
# Profile route
@app.route("/profile",methods=["GET"])
@token_required
def profile(payload):
    pass
# Users route - get all users
@app.route("/users",methods=["GET"])
def users():
    pass
# Entry point
if __name__=="__main__":
    init_db()
    app.run(debug=True)
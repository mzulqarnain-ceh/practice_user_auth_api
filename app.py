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
    data=request.get_json()
    if not data or "username" not in data or "email" not in data or "password" not in data:
        return jsonify({"error":"Every field username,email and password must be filled"}),400
    conn=get_db_connection()
    user=conn.execute("SELECT * FROM users WHERE username=? OR email=?",(data["username"],data["email"],)).fetchone()
    if user:
        conn.close()
        return jsonify({"error":"username or email already exists"}),400
    hash=generate_password_hash(data["password"])
    conn.execute("INSERT INTO users (username,email,password_hash) VALUES(?,?,?)",(data["username"],data["email"],hash,))
    conn.commit()
    conn.close()
    return jsonify({"message":"user created successfully"}),201
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
import jwt
from functools import wraps
from flask import Flask,jsonify,request
from config import SECRET_KEY
# decorayor function
def token_required():
    pass

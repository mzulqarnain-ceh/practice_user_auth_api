import jwt
from functools import wraps
from flask import Flask,jsonify,request
from config import SECRET_KEY
# decorayor function
def token_required(f):
    # wrapper function
    @wraps(f)
    def decorate(*args,**kwargs):
        token=request.headers.get("Authorization")
        if not token:
            return jsonify({"error":"Token is missing"}),401
        parts=token.split(" ")
        if len(parts) !=2 or parts[0].lower != "bearer":
            return jsonify({"error":"Invalid token format. Must be 'Bearer <token>'"}),401
        token=parts[1]
        try:
            payload=jwt.decode(token,SECRET_KEY,algorithm=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error":"Token Expired"}),401
        except jwt.InvalidTokenError:
            return jsonify({"error":"Invalid Token"}),401
        return f(payload,*args,**kwargs)
    return decorate
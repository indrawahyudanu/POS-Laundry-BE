from flask import Blueprint
from flask import jsonify
from flask import request

auth_bp = Blueprint('auth', __name__)

# Endpoint: POST /api/auth/register
@auth_bp.route('/register', methods=['POST'])
def register():
    data=request.get_json()

    return jsonify({"message" : "Register Berhasil",
                    "user" : data}), 201

# Endpoint: POST /api/auth/login
@auth_bp.route('/login', methods = ['POST'])
def login_user():
    data=request.get_json()

    return jsonify({"message":"Login Berhasil",
                    "token" : "tokendumy"}), 200
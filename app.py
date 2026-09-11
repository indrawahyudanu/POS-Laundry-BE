from flask import Flask,jsonify
from routes.auth_routes import auth_bp

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix='/api/auth')

@app.route('/')
def home():
    return "Hello"

if __name__== '__main__':
    app.run(debug=True)


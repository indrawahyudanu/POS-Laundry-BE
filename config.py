import os

from dotenv import load_dotenv

load_dotenv()

class config :
    SQLALCHEMY_DATABSE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = os.getenv('SECRET_KEY','default_secret_key_laundry')

    
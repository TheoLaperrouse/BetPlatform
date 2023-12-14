import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") or ''
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") or 'back'
JWT_EXPIRATION_TIME = int(os.getenv("JWT_EXPIRATION_TIME")) or 60

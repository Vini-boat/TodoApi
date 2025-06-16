from dotenv import load_dotenv
import os

load_dotenv()

# database
DATABASE_URL = os.getenv("DATABASE_URL")

# jwt

SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# passlib
HASH_ALGORITHM = os.getenv("HASH_ALGORITHM")

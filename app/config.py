from dotenv import load_dotenv
import os

load_dotenv()

# database
DATABASE_URL = os.getenv("DATABASE_URL")

# jwt

# passlib
HASH_ALGORITHM = os.getenv("HASH_ALGORITHM")
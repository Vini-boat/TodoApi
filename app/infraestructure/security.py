from passlib.context import CryptContext
from app.config import HASH_ALGORITHM

# WHY: resolve o aviso "AttributeError: module 'bcrypt' has no attribute '__about__'"
# https://github.com/pyca/bcrypt/issues/684#issuecomment-2430047176
import bcrypt
from dataclasses import dataclass

@dataclass
class SolveBugBcryptWarning:
    __version__: str = getattr(bcrypt, "__version__")

setattr(bcrypt, "__about__", SolveBugBcryptWarning())
# WHY: resolve o aviso "AttributeError: module 'bcrypt' has no attribute '__about__'"

pwd_context = CryptContext(schemes=[HASH_ALGORITHM], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

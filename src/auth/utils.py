from argon2 import PasswordHasher

def hash_password(password: str) -> str:
    ph = PasswordHasher()
    password_hash = ph.hash(password)
    return password_hash

def verify_password(password: str, password_hash: str) -> bool:
    ph = PasswordHasher()
    result = ph.verify(password_hash, password)
    return result
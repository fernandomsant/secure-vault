from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import HKDF, scrypt
from typing import BinaryIO
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import tempfile
import os

SALT_SIZE = 16
NONCE_SIZE = 12

def encrypt_file(file: BinaryIO, file_description: str, size: int, output_path: str, password: str, chunk_size: int = 64*1024) -> str:
    file_description = file_description.encode('utf-8')
    description_size = bytes([len(file_description)])
    salt = get_random_bytes(SALT_SIZE)
    nonce = get_random_bytes(NONCE_SIZE)
    key = scrypt(password, salt, key_len=32, N=2**20, r=8, p=1)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    processed = 0
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as fout:
        fout.write(salt)
        fout.write(nonce)
        fout.write(description_size)
        encrypted_description = cipher.encrypt(file_description)
        fout.write(encrypted_description)
        while processed < size:
            chunk = file.read(min(chunk_size, size - processed))
            encrypted_chunk = cipher.encrypt(chunk)
            fout.write(encrypted_chunk)
            processed += len(chunk)
        tag = cipher.digest()
        print(tag)
        fout.write(tag)
    return output_path

def decrypt_file(file_path: str, password: str, chunk_size=64*1024):
    with tempfile.TemporaryFile(mode='w+b') as tmp, open(file_path, 'rb') as f:
        salt = f.read(SALT_SIZE)
        nonce = f.read(NONCE_SIZE)
        description_size = int.from_bytes(f.read(1))
        key = scrypt(password, salt, key_len=32, N=2**20, r=8, p=1)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        file_description = cipher.decrypt(f.read(description_size))
        f.seek(0, 2)
        file_size = f.tell()
        f.seek(SALT_SIZE + NONCE_SIZE + 1 + description_size)
        encrypted_size = file_size - SALT_SIZE - NONCE_SIZE - 1 - description_size - 16
        remaining = encrypted_size
        while remaining > 0 :
            chunk = f.read(min(chunk_size, remaining))
            tmp.write(cipher.decrypt(chunk))
            remaining -= len(chunk)
        tag = f.read(16)
        cipher.verify(tag)
        yield file_description
        tmp.seek(0)
        remaining = encrypted_size
        while remaining > 0:
            chunk = tmp.read(min(chunk_size, remaining))
            yield chunk
            remaining -= len(chunk)
        return
import base64
import json
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

SALT_FILE = "salt.bin"
ENC_FILE = "storage.enc"
ITERATIONS = 100_000


def get_salt():
    if not os.path.exists(SALT_FILE):
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    else:
        with open(SALT_FILE, "rb") as f:
            salt = f.read()
    return salt


def derive_key(master_password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend(),
    )
    return kdf.derive(master_password.encode())


def encrypt_data(data: dict, key: bytes):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    json_data = json.dumps(data).encode()
    ciphertext = aesgcm.encrypt(nonce, json_data, None)
    return base64.b64encode(nonce + ciphertext).decode()


def decrypt_data(encrypted_data: str, key: bytes):
    raw_data = base64.b64decode(encrypted_data.encode())
    nonce, ciphertext = raw_data[:12], raw_data[12:]
    aesgcm = AESGCM(key)
    json_data = aesgcm.decrypt(nonce, ciphertext, None)
    return json.loads(json_data)


def save_encrypted(data: dict, key: bytes):
    encrypted = encrypt_data(data, key)
    with open(ENC_FILE, "w") as f:
        f.write(encrypted)


def load_encrypted(key: bytes):
    if not os.path.exists(ENC_FILE):
        return {}
    with open(ENC_FILE, "r") as f:
        encrypted = f.read()
    return decrypt_data(encrypted, key)

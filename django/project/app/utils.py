import requests
# withdraw
import os
import hashlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from django.conf import settings

def get_azampay_token():
    url = "https://authenticator-sandbox.azampay.co.tz/AppRegistration/GenerateToken"
    headers = {"Content-Type": "application/json"}
    payload = {
        "appName": "",
        "clientId": "",
        "clientSecret": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        access_token = response.json().get("data", {}).get("accessToken")
        print("✅ Token Generated Successfully:", access_token)
        return access_token

    return None



def generate_checksum(input_string: str) -> str:
    """
    Generates a checksum by hashing input string with SHA-512,
    encrypting with RSA public key, and encoding in Base64.
    """
    if not os.path.exists(settings.PUBLIC_KEY_PATH):
        raise FileNotFoundError(f"🔴 Public key file not found at: {settings.PUBLIC_KEY_PATH}")

    # Load the public key
    with open(settings.PUBLIC_KEY_PATH, 'rb') as key_file:
        public_key = RSA.import_key(key_file.read())

    # Step 1: Create SHA-512 Hash
    sha512_hash = hashlib.sha512(input_string.encode()).digest()

    # Step 2: Encrypt using RSA PKCS1 Padding
    cipher = PKCS1_v1_5.new(public_key)
    encrypted_data = cipher.encrypt(sha512_hash)

    # Step 3: Encode in Base64
    base64_checksum = base64.b64encode(encrypted_data).decode()

    return base64_checksum

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
        "appName": "McColn",
        "clientId": "f5f66619-bfd8-4375-8b79-0b7caa642692",
        "clientSecret": "UolIKZlt6xsQN+sChnuHXCbcq8eosrhXqVrHQPHZN8wf0fqw38I0utYzTboLiGKvUfOJefs9P5CCzxk5dAD9y9N4+i+AQUwiV5H/Bh+7Qf8bnC0Rlab4JKa+NVhajWbMhItY8/+KDhAK2rRMx2Matt1DhCZOJhksKcnn1FYTlJTuxdUUrthihjLYeNl0vgltbJrJ3tXKiM/0PNZo2IsvqxH08MQAE8GOP2LOYeoCzSh1V+U1GPva00nwnDJ4R1kmwRweAOj7YE+MdpV36SK92yjJx1hm8k0qnml72S3Wbr+oKZRnOKG7FxBcv3J4evOpK4RijaI2hCoBxHtSaWPFghg+bVtfpZJExbrYXGhQ0TjmjSj5AmSatA7ohoUvM468mW0GfDMnPJg/ycNsC/j53MbK5RGK/0XVf4hYhen3A+udqDpSNz7ptByim21RAc+AuC7u5s7SJKZT6Ten/lbFMDgu8BUcK9WxP/DR5cPRiEwvGA28pvKrKnwM1NcEiDK8s2q/1ngYXZTNo6FkmraShohG3dui+D0RnU8sTWMjz2x2QkghPn/40plkIv6nMbtjtnHGZTns3Wi7YBsoGHrrn7uprQZGq4y/yS7WmqNrTBJ88s5QL4OtK/+IUZeySqkh2PR6B7yIp9hTFkAnisg5SPl8/DCxTN5Kkxsg3INE53g="
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

import requests

# Step 1: Define API URLs
# base_url = "https://sandbox.azampay.co.tz"
token_url = "https://authenticator-sandbox.azampay.co.tz/AppRegistration/GenerateToken"
checkout_url = "https://sandbox.azampay.co.tz/azampay/mno/checkout"

# Step 2: API credentials (Replace with actual values)
credentials = {
        "appName": "McColn",
        "clientId": "f5f66619-bfd8-4375-8b79-0b7caa642692",
        "clientSecret": "FZpjnMnIUf/C5n3e9xk2R2t48eTM4qvdb53f1Cnl7CqO2ojDMfVu9Udsx6YJiHKtRxbsKfVuRoA8oetTGOzD13GtyfVbYthZdzrS7s8hWwXP9lnWRR13EPE3Tf04hU98aynXbgZ5mZkvGGwNTOUI8yCcVfEimTCgMIgRYOCXD+VJ3Gwqlgi4kIoDz9z7eRPnOlTJbRaNDjezU5uX0GaM2vx3mHECsA/KoPPSNFlTE6UXIZJKXSuPxaaYxwMs0QmlLcx6sIh3mJeua7Gg7kdRs0kWzI6WYDHn2vivYzxrY+Di7HFn5j1y9fS8kQYAEbGipjyXGLzFK2/FBn4L2xT+fdVBgRFmGPp4XvVttTL7FOUNibl3l2SuzYq0ddIlTAde108xI8vgE7ln6umyRBI/9gJloVaMbGHwlQHuxVeZF3NYGQEWvIBjK9Wzazha/tUAjx7vaCuM7v/CgUb6Ml/2uDS7e+/UAbY0+tHiHfHXQ9FRrLCd1+aI08idflbEM0xSqeXVOIZ9JTR/J2PogRRCa5yoO7sGyok868kyghQBoKKYoMzukgOyvgAszBhGE34pHALF2aKC2a/mRR5/9AqhNf/yPhI246Tqg7fb1NE+zc52wBFKJTU6UcdVSkgLtuABsZjNPKSKLlfLfX9wmtcuW7cPF5uN5pFEaX7tycgzeEk="
    }

# Step 3: Request Token
headers = {"Content-Type": "application/json"}
token_response = requests.post(token_url, json=credentials, headers=headers)

if token_response.status_code == 200:
    access_token = token_response.json().get("data", {}).get("accessToken")  # Extract token
    print("✅ Token Generated Successfully:", access_token)
else:
    print("❌ Failed to generate token:", token_response.text)
    exit()  # Stop script if token generation fails

# Step 4: Prepare Checkout Request
checkout_payload = {
    "accountNumber": "255748121594",  # Replace with actual phone number
    "additionalProperties": {
        "property1": None,
        "property2": None
    },
    "amount": "1000",  # Replace with actual amount
    "currency": "TZS",  # TZS for Tanzanian Shilling
    "externalId": "123456",  # Unique transaction ID
    "provider": "Mpesa"  # Can be Airtel, Tigo, Vodacom
}

checkout_headers = {
    "Authorization": f"Bearer {access_token}",  # Use generated token
    "Content-Type": "application/json"
}

# Step 5: Send Checkout Request
checkout_response = requests.post(checkout_url, json=checkout_payload, headers=checkout_headers)

# Step 6: Print Response
print("🔄 Checkout API Response:")
print("Status Code:", checkout_response.status_code)
print("Response:", checkout_response.json())

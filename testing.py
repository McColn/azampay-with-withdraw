

import requests

url = "https://authenticator-sandbox.azampay.co.tz/AppRegistration/GenerateToken"  # Ensure this is correct

payload = {
        "appName": "McColn",
        "clientId": "f5f66619-bfd8-4375-8b79-0b7caa642692",
        "clientSecret": "FZpjnMnIUf/C5n3e9xk2R2t48eTM4qvdb53f1Cnl7CqO2ojDMfVu9Udsx6YJiHKtRxbsKfVuRoA8oetTGOzD13GtyfVbYthZdzrS7s8hWwXP9lnWRR13EPE3Tf04hU98aynXbgZ5mZkvGGwNTOUI8yCcVfEimTCgMIgRYOCXD+VJ3Gwqlgi4kIoDz9z7eRPnOlTJbRaNDjezU5uX0GaM2vx3mHECsA/KoPPSNFlTE6UXIZJKXSuPxaaYxwMs0QmlLcx6sIh3mJeua7Gg7kdRs0kWzI6WYDHn2vivYzxrY+Di7HFn5j1y9fS8kQYAEbGipjyXGLzFK2/FBn4L2xT+fdVBgRFmGPp4XvVttTL7FOUNibl3l2SuzYq0ddIlTAde108xI8vgE7ln6umyRBI/9gJloVaMbGHwlQHuxVeZF3NYGQEWvIBjK9Wzazha/tUAjx7vaCuM7v/CgUb6Ml/2uDS7e+/UAbY0+tHiHfHXQ9FRrLCd1+aI08idflbEM0xSqeXVOIZ9JTR/J2PogRRCa5yoO7sGyok868kyghQBoKKYoMzukgOyvgAszBhGE34pHALF2aKC2a/mRR5/9AqhNf/yPhI246Tqg7fb1NE+zc52wBFKJTU6UcdVSkgLtuABsZjNPKSKLlfLfX9wmtcuW7cPF5uN5pFEaX7tycgzeEk="
    }
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

# Debugging: Print status and raw response
print("Status Code:", response.status_code)

# Extract and print accessToken
if response.status_code == 200:
    try:
        access_token = response.json().get("data", {}).get("accessToken")  # Extract token
        if access_token:
            print("Access Token:", access_token)
        else:
            print("Error: Access Token not found in response.")
    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not in JSON format.")
else:
    print("Failed to get token. Check API credentials and URL.")


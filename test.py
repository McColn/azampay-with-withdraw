import requests

def get_azampay_token():
    url = "https://authenticator-sandbox.azampay.co.tz/AppRegistration/GenerateToken"
    headers = {"Content-Type": "application/json"}
    payload = {
        "appName": "McColn",
        "clientId": "f5f66619-bfd8-4375-8b79-0b7caa642692",
        "clientSecret": "OclYode5g4LECjU604Mf0KEMQO6eDh8ZX9EEY8SiT86FqJ7rgBOzEWz1+2fZJgdJ+A12ZR1TUlrH/uh5AXAbYgus1Nw9RqYbAy6iT3RMQvyb0/YYhZxiM1t6rHo5fb+ySk7md3wmB95X/gITPVWCF53vv1dxzicVIa0XkcuINqwD3LCCW7v67EaL2mG3WezhKFWQ0XCdilnIRgP14eQwiPDjjJahQOUk3PeRv5l/qNwVUORDNZQ7Aa15LXpSMaozqNawhU6TYjBvpIgyeHM9ZlyWkKGoTsmT190hyERBLM/b7/a9/li08qhoj01CG6L6cYyA8Oa7UJHxdTsXHHRLCgKRE+Go0hfNNuDLZoGJrS2b3RM4auC0+26cZ+NDiTDM8YkrA++cQUTzFMNVzXHfidpFwgWbdSAOmebwYsjX8gZn6hmX7l0X6O0IE6qCP8rqchKg3kki2T0g7fkiuzcjxRIAU/fDkfRQgAQVGy3FI7rMbj+nMVlOFqa3+omWRwsQcNEZHmRQLuFF8BFgyolAQ8miN3R2R1EawRZsxewvL3IRhQmO7Xqfe/XkByWt97k2Yn7BzZEDvZTDshOeBd26Z6anOGI+yCLE/ztrV/e+4yH+ZJjx33AHHFJzOj3CFZ1ueNfHRpJceydIhWQlVxA5JorWDSYThwp0+ivVbOy+vdo="
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        access_token = response.json().get("data", {}).get("accessToken")
        print("✅ Token Generated Successfully:", access_token)
        return response.json().get("accessToken")

    return None

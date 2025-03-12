from Crypto.PublicKey import RSA

# Generate a 2048-bit RSA key pair
key = RSA.generate(2048)

# Save the private key
with open("private_key.pem", "wb") as private_file:
    private_file.write(key.export_key())

# Save the public key
with open("public_key.pem", "wb") as public_file:
    public_file.write(key.publickey().export_key())

print("✅ RSA Key Pair Generated: public_key.pem & private_key.pem")

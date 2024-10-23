from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Load the private RSA key (in PEM format)
with open("id_rsa", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,  # Replace with password if the key is encrypted
        backend=default_backend()
    )

# Extract the public key from the private key
public_key = private_key.public_key()

# Convert the public key to PEM format for easy saving or display
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save or print the public key in PEM format
with open("public_key.pem", "wb") as public_key_file:
    public_key_file.write(public_pem)

print(public_pem.decode("utf-8"))

from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Generate private and public keys
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = input("Enter message: ").encode()

# Generate digital signature
signature = private_key.sign(
    message,
    hashes.SHA256()
)

print("Digital Signature:", signature.hex())

# Verify digital signature
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )
    print("Signature Verified: Message is authentic")

except Exception:
    print("Signature Verification Failed: Message is invalid")
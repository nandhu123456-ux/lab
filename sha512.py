import hashlib

text = input("Enter message: ")

# Generate SHA-512 hash
hash_value = hashlib.sha512(text.encode()).hexdigest()

print("SHA-512 Hash:", hash_value)
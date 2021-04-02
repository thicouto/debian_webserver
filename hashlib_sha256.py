from hashlib import sha256
password_sha = "string_to_sha256"
password_sha = sha256(password_sha.encode('utf-8')).hexdigest()
print(password_sha)

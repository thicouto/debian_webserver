from hashlib import sha256
password_sha = "mainofc2021"
password_sha = sha256(password_sha.encode('utf-8')).hexdigest()
print(password_sha)

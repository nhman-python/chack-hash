import hashlib

def verify_hash(file_path, original_hash):
    with open(file_path, 'rb') as f:
        data = f.read()
        sha256 = hashlib.sha256()
        sha256.update(data)
        file_hash = sha256.hexdigest()
        return file_hash == original_hash

file_path = input("Enter the file path: ")
original_hash = input("Enter the original hash: ")

if verify_hash(file_path, original_hash):
    print("The hash is correct.")
else:
    print("The hash is incorrect.")

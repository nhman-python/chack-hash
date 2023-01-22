import hashlib

def verify_hash(file_path, original_hash, algorithm):
    hash_algorithms = {'md5': hashlib.md5(), 'sha1': hashlib.sha1(), 'sha256': hashlib.sha256(), 'sha512': hashlib.sha512()}
    if algorithm not in hash_algorithms:
        raise ValueError(f"{algorithm} is not supported, the supported algorithms are md5, sha1, sha256, sha512")
    
    with open(file_path, 'rb') as f:
        data = f.read()
        hash_algorithm = hash_algorithms[algorithm]
        hash_algorithm.update(data)
        file_hash = hash_algorithm.hexdigest()
        return file_hash == original_hash

file_path = input("Enter the file path: ")
original_hash = input("Enter the original hash: ")
algorithm = input("Enter the hash algorithm to use (md5, sha1, sha256, sha512): ")
print("Please wait, it will take some time to verify the file. In the meantime you can go out for coffee :)")

if verify_hash(file_path, original_hash, algorithm):
    print(f"The {algorithm} hash is correct.")
else:
    print(f"The {algorithm} hash is incorrect.")

import hashlib

def generate_file_hash(filename, hash_algo='sha256'):
    try:
        with open(filename, 'rb') as file:
            data = file.read()
            if hash_algo.lower() == 'sha256':
                file_hash = hashlib.sha256(data).hexdigest()
            elif hash_algo.lower() == 'md5':
                file_hash = hashlib.md5(data).hexdigest()
            else:
                raise ValueError("Unsupported hash algorithm.")
            return file_hash
    except FileNotFoundError:
        return "File not found."

def verify_file_hash(filename, original_hash, hash_algo='sha256'):
    current_hash = generate_file_hash(filename, hash_algo)
    if current_hash == original_hash:
        return True
    return False

if __name__ == "__main__":
    print("==== File Hash Generator & Verifier ====")
    file_path = input("Enter the path to the file: ")
    print("Choose hash algorithm (md5 / sha256): ", end='')
    algo = input().strip().lower()

    print("\n1. Generate hash")
    print("2. Verify hash")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        file_hash = generate_file_hash(file_path, algo)
        print(f"\nGenerated {algo.upper()} Hash: {file_hash}")
    elif choice == '2':
        original_hash = input("Enter the original hash to verify: ").strip()
        if verify_file_hash(file_path, original_hash, algo):
            print("\n✅ Hash Verified: File is intact.")
        else:
            print("\n❌ Hash Mismatch: File may have been tampered with.")
    else:
        print("Invalid choice.")
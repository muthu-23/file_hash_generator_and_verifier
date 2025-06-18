 🔐 File Hash Generator & Verifier

A lightweight command-line utility to generate and verify cryptographic hashes (MD5 and SHA256) of files. This tool is useful for verifying file integrity and detecting unauthorized modifications — a common practice in cybersecurity workflows.

---

## 🚀 Features

- Generate file hashes using MD5 or SHA256
- Verify file integrity against a given hash
- CLI-based interaction for simplicity and portability
- Minimal dependencies — works out of the box with Python 3

---

## 📦 Requirements

- Python 3.6 or above

---




💻 Sample Output

Example Output 1: Generate Hash using MD5

==== File Hash Generator & Verifier ====
Enter the path to the file: example.txt
Choose hash algorithm (md5 / sha256): md5

1. Generate hash
2. Verify hash
Enter your choice (1 or 2): 1

✅ Generated MD5 Hash: 5d41402abc4b2a76b9719d911017c592


---

 Example Output 2: Verify Hash using SHA256 (Match Success)

==== File Hash Generator & Verifier ====
Enter the path to the file: example.txt
Choose hash algorithm (md5 / sha256): sha256

1. Generate hash
2. Verify hash
Enter your choice (1 or 2): 2
Enter the original hash to verify: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

✅ Hash Verified: File is intact.


---

 Example Output 3: Verify Hash using MD5 (Mismatch / Tampered File)

==== File Hash Generator & Verifier ====
Enter the path to the file: example.txt
Choose hash algorithm (md5 / sha256): md5

1. Generate hash
2. Verify hash
Enter your choice (1 or 2): 2
Enter the original hash to verify: 1234567890abcdef1234567890abcdef

❌ Hash Mismatch: File may have been tampered with.


---

📁 Folder Structure

File_Hash_Generator_Verifier/

├── example.txt            # sample test file

├── hash_verifier.py       # Main script

└── README.md              # Project documentation


---

👤 Author

Muthusamy T.

B.sc computer science (Cybersecurity) Student @ Vels University, Chennai

GitHub: muthu-23


---

🤝 Contributions

Contributions, suggestions, or improvements are welcome. Please open an issue or submit a pull request.

---

⭐ Star This Repository

If you found this helpful or educational, consider giving it a ⭐ to support this project and share with others!

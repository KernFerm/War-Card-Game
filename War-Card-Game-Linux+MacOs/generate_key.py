
import os
import sys
from cryptography.fernet import Fernet

key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "win-results.key")

def error(msg):
    print(f"[ERROR] {msg}")
    exit(1)

# Security: refuse to write to symlink or non-regular file
if os.path.exists(key_path):
    if os.path.islink(key_path):
        error(f"Refusing to overwrite symlink: {key_path}")
    if not os.path.isfile(key_path):
        error(f"Refusing to overwrite non-regular file: {key_path}")
    # Confirm before overwriting
    try:
        resp = input(f"Key file already exists at {key_path}. Overwrite? (y/N): ").strip().lower()
    except EOFError:
        resp = 'n'
    if resp != 'y':
        print("Aborted. Key not overwritten.")
        exit(0)

key = Fernet.generate_key()
with open(key_path, "wb") as f:
    f.write(key)
print(f"New Fernet key generated and saved to {key_path}.")

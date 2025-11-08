import os
import json
from cryptography.fernet import Fernet, InvalidToken

import sys
key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "win-results.key")
results_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "win-results.json")

def error(msg):
    print(f"[ERROR] {msg}")
    exit(1)

# Check file existence
if not os.path.exists(key_path):
    error("Key file does not exist.")
if not os.path.exists(results_path):
    error("Results file does not exist.")

with open(key_path, "rb") as kf:
    key = kf.read()
if len(key) != 44:
    error("Key file is not a valid Fernet key (44 bytes).")
try:
    fernet = Fernet(key)
except Exception:
    error("Key is not a valid Fernet key.")

with open(results_path, "rb") as rf:
    encrypted = rf.read()
if not encrypted:
    error("Results file is empty.")
try:
    decrypted = fernet.decrypt(encrypted)
except InvalidToken:
    error("Failed to decrypt results: Invalid key or corrupted file.")
except Exception as e:
    error(f"Failed to decrypt results: {e}")
try:
    data = json.loads(decrypted)
except Exception:
    error("Decrypted data is not valid JSON.")
if not isinstance(data, list):
    error("Decrypted results is not a list.")
print(json.dumps(data, indent=2))
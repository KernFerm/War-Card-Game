# Card Game War

![Python](https://img.shields.io/badge/Python-3.11.9-blue?logo=python)
![Windows](https://img.shields.io/badge/Windows-Supported-blue?logo=windows)
![Cross-Platform](https://img.shields.io/badge/Cross--Platform-Yes-green?logo=linux)
![Encryption](https://img.shields.io/badge/Security-Fernet-green?logo=lock)
![Pyarmor](https://img.shields.io/badge/Obfuscated-Pyarmor%209.1.9-orange?logo=python)

## 🎮 Overview

Welcome to the Card Game War project! This project provides a secure, cross-platform implementation of the classic card game "War" with a graphical interface and encrypted results storage.


**How it works:**
- Key files (`war.py`, etc.) are obfuscated and require the `pyarmor_runtime_007668` runtime folder to run.
- The runtime is included in the project and loaded automatically.
- This helps protect your code and intellectual property.

**How to use:**
- Run scripts as usual (e.g., `python war.py`).
- Do not delete or move the `pyarmor_runtime_007668` folder.


| File                | Purpose                                                                 |
|---------------------|------------------------------------------------------------------------|
| `war.py`            | Main GUI for playing War. Handles game logic, encryption, user input. Obfuscated with Pyarmor.|
| `generate_key.py`   | Generates a secure Fernet key for encrypting results.                   |
| `decrypt_results.py`| Decrypts and reads the encrypted results file.                          |
| `win-results.json`  | Stores encrypted game results.                                          |
| `win-results.key`   | Stores the Fernet encryption key.                                       |

## 🚀 How to Use


### 1️⃣ Setup
1. **Install Python 3.11.9**
---
# [Python 3.11.9 arm64 & amd64](https://github.com/KernFerm/War-Card-Game/releases/tag/python3119amd64arm64)
---

#### 🪟 Windows
- Download Python from the official website: [python.org/downloads](https://www.python.org/downloads/windows/)
- Run the installer and check "Add Python to PATH" during setup.
- Verify installation:
    ```powershell
    python --version
    ```


#### 🐧 Linux
- Most Linux systems already come with Python pre-installed. You can use the default version that comes with your distribution.
- If you are having issues download the Python Version `3.11.9`.
- To check your Python version:
    ```bash
    python3 --version
    ```
- If you need to install or upgrade Python, use your package manager (example for Ubuntu/Debian):
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    python3 --version
    ```

#### 🍎 macOS
- Download Python from [python.org/downloads](https://www.python.org/downloads/macos/)
- Or use Homebrew:
    ```bash
    brew install python
    python3 --version
    ```

2. Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

### 2️⃣ Generate Encryption Key
Run the key generator:
```bash
python generate_key.py
```


### 3️⃣ Play the Game
Start the GUI:
```bash
python war.py --gui
```

### 🖥️ Play the Console Version
To play the classic text-based version in your terminal:
```bash
python war.py
```

### 4️⃣ View Results
Decrypt and view results:
```bash
python decrypt_results.py
```


## 🖥️ Windows Quick Start
Double-click `run.bat` to:
- Generate the key (if missing)
- Choose to play the GUI or Console version from a menu

## 🏁 Cross-Platform Support
All `.py` files use `os` and `sys` for path handling and are compatible with Windows, macOS, and Linux. No platform-specific code is used.

## 📝 Notes
- Make sure `win-results.key` and `win-results.json` are in the same directory as the scripts.
- For Linux/macOS, use the same commands in your terminal.

---
Made with ❤️ by the BubblesTheDev!


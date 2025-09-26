@echo off
REM Card Game War Launcher
REM Always run from the script's directory (project root)
cd /d "%~dp0"

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b 1
)

REM Check for required files
if not exist requirements.txt (
    echo [ERROR] requirements.txt missing. Please restore it.
    pause
    exit /b 1
)

REM Install dependencies (if pip available)
pip --version >nul 2>&1
if not errorlevel 1 (
    pip install -r requirements.txt
)

REM Generate key if missing
if not exist win-results.key (
    python generate_key.py
)

REM Check for tampering (basic)
for %%F in (war.py generate_key.py decrypt_results.py) do (
    if not exist %%F (
        echo [ERROR] %%F missing. Aborting.
        pause
        exit /b 1
    )
)

REM Menu to choose version
echo.
echo Card Game War Launcher
echo ======================
echo 1. Play GUI version
echo 2. Play Console version
echo 3. Exit
set /p choice="Select an option (1-3): "
if "%choice%"=="1" (
    python war.py --gui
    goto :eof
)
if "%choice%"=="2" (
    python war.py
    goto :eof
)
if "%choice%"=="3" (
    exit /b 0
)
echo Invalid choice. Exiting.
exit /b 1
python war.py

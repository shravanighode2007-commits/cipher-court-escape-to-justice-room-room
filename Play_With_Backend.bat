@echo off
title Cipher Court - Full Experience Launcher
cd /d "%~dp0"

echo ==============================================================
echo        CIPHER COURT: ESCAPE TO JUSTICE - FULL LAUNCHER
echo ==============================================================
echo [1/3] Starting Telemetry Web Server & Database on Port 8000...
start "Cipher Court Backend" /min cmd /c "cd Backend && python server.py"

echo [2/3] Opening Live Audit Log Dashboard in Browser...
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8000"

echo [3/3] Launching Cipher Court Standalone Game...
if exist "Builds\CipherCourt_Windows_x64\CipherCourt.exe" (
    start "" "Builds\CipherCourt_Windows_x64\CipherCourt.exe"
    echo.
    echo Game and Backend are now running!
    echo - Press [F1] in-game to view the In-Game Telemetry Viewer.
    echo - Switch to your web browser to view the Live Web Dashboard.
    echo.
) else (
    echo [ERROR] Game executable not found at: Builds\CipherCourt_Windows_x64\CipherCourt.exe
    pause
)

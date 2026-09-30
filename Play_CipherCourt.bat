@echo off
title Cipher Court - Escape to Justice
cd /d "%~dp0"

echo ==============================================================
echo              CIPHER COURT: ESCAPE TO JUSTICE
echo ==============================================================
echo Launching Cipher Court Standalone Game...
echo.

if exist "Builds\CipherCourt_Windows_x64\CipherCourt.exe" (
    start "" "Builds\CipherCourt_Windows_x64\CipherCourt.exe"
) else (
    echo [ERROR] Game executable not found at: Builds\CipherCourt_Windows_x64\CipherCourt.exe
    pause
)

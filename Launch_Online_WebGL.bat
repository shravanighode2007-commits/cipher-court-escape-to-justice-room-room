@echo off
title Cipher Court - Live Online WebGL Deployment
cd /d "%~dp0"

echo ==============================================================
echo       CIPHER COURT: LIVE ONLINE BROWSER DEPLOYMENT
echo ==============================================================
echo Launching WebGL server & secure public HTTPS tunnel...
echo.
python deploy_online.py
pause

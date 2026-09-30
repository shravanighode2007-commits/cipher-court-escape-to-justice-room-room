@echo off
setlocal enabledelayedexpansion
title Push Cipher Court to GitHub
cd /d "%~dp0"

set "GIT_EXE=git"
where git >nul 2>nul
if errorlevel 1 (
    if exist "C:\Users\Laxman\AppData\Local\Programs\MinGit\cmd\git.exe" (
        set "GIT_EXE=C:\Users\Laxman\AppData\Local\Programs\MinGit\cmd\git.exe"
    ) else if exist "C:\Users\Laxman\AppData\Local\github-copilot-git-2.53.0-4\cmd\git.exe" (
        set "GIT_EXE=C:\Users\Laxman\AppData\Local\github-copilot-git-2.53.0-4\cmd\git.exe"
    )
)

echo ==============================================================
echo         PUSH CIPHER COURT REPOSITORY TO GITHUB
echo ==============================================================
echo Current Branch: main
echo.
set /p "REPO_URL=Enter your GitHub Repo URL (e.g. https://github.com/YOUR_USERNAME/cipher-court.git): "

if "!REPO_URL!"=="" (
    echo [ERROR] No repository URL was entered.
    pause
    exit /b 1
)

echo.
echo [*] Setting remote origin to !REPO_URL!...
"!GIT_EXE!" remote remove origin 2>nul
"!GIT_EXE!" remote add origin "!REPO_URL!"
"!GIT_EXE!" branch -M main

echo [*] Pushing main branch to GitHub...
"!GIT_EXE!" push -u origin main

if errorlevel 1 (
    echo.
    echo [!] Push encountered an issue. Ensure:
    echo     1. The GitHub repository is created.
    echo     2. You have permission / are logged into GitHub.
) else (
    echo.
    echo [SUCCESS] Repository pushed to GitHub!
)
pause

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
set "DEFAULT_REPO=https://github.com/shravanighode2007-commits/cipher-court-escape-to-justice-room-room.git"
echo Target Repository:
echo   !DEFAULT_REPO!
echo.
set /p "REPO_URL=Press ENTER to push to this repository (or enter a new URL): "
if "!REPO_URL!"=="" set "REPO_URL=!DEFAULT_REPO!"

echo.
echo [*] Setting remote origin to !REPO_URL!...
"!GIT_EXE!" remote remove origin 2>nul
"!GIT_EXE!" remote add origin "!REPO_URL!"
"!GIT_EXE!" branch -M main

echo.
echo [*] Pushing main branch to GitHub...
echo (If prompted, log into GitHub in the browser window or enter your Personal Access Token)
echo.
"!GIT_EXE!" push -u origin main

if errorlevel 1 (
    echo.
    echo [!] Push encountered an authentication or network notice.
    echo     If GitHub asked for a password, note that GitHub requires a Personal Access Token (PAT).
    echo     You can generate one with 'repo' scope at: https://github.com/settings/tokens
) else (
    echo.
    echo ==============================================================
    echo [SUCCESS] CIPHER COURT IS NOW LIVE ON GITHUB!
    echo Repository: !REPO_URL!
    echo ==============================================================
)
echo.
pause

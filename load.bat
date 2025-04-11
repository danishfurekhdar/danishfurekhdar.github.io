@echo off
cd /d "C:\Users\furkh\Downloads\danishfurekhdar.github.io-1eec030f2db77b4a625bc74a54481111921a4a84\danishfurekhdar.github.io-1eec030f2db77b4a625bc74a54481111921a4a84"

REM Initialize git only if not already initialized
IF NOT EXIST ".git\config" (
    git init
)

REM Ensure origin is set correctly
git remote remove origin 2>nul
git remote add origin https://github.com/danishfurekhdar/danishfurekhdar.github.io

REM Set main branch just in case
git branch -M main

REM Pull remote content and rebase
git pull --rebase origin main

REM Stage and commit changes
git add .
git diff --cached --quiet || git commit -m "Upload/update full blog directory"

REM Push to GitHub
git push origin main

pause

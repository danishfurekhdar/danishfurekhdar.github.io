@echo off
cd /d "C:\Users\furkh\Downloads\danishfurekhdar.github.io-1eec030f2db77b4a625bc74a54481111921a4a84\danishfurekhdar.github.io-1eec030f2db77b4a625bc74a54481111921a4a84"

REM Initialize Git (if not already)
IF NOT EXIST ".git\config" (
    git init
)

REM Force set remote origin
git remote remove origin 2>nul
git remote add origin https://github.com/danishfurekhdar/danishfurekhdar.github.io

REM Set branch to main
git branch -M main

REM Stage all files
git add -A

REM Make commit (no error if nothing changed)
git commit -m "Initial force upload of full site" 2>nul

REM Force push to remote (overwrite everything there)
git push --force origin main

pause

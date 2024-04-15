@echo off

rem Check if pyautogui is installed
pip show pyautogui >nul 2>&1

if %errorlevel% neq 0 (
  echo Installing pyautogui...
  pip install pyautogui
) else (
  echo pyautogui is already installed.
)

rem Run your Python script
python script.py
pause

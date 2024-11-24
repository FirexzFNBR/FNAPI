@echo off
REM 
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python not found.
    exit /b 1
)

REM 
echo Downloading requirements.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Done! Now open 'startprogram' to use FNAPI 1.2.1
pause

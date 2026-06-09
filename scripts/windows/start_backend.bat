@echo off
echo Starting Optimized Fish Speech Backend...
echo.

cd /d "%~dp0..\.."

REM Deactivate conda if active
call conda deactivate 2>nul

REM Activate .venv (created by uv)
if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
    echo Using .venv (uv)
) else if exist venv312\Scripts\activate.bat (
    call venv312\Scripts\activate.bat
    echo Using venv312 (Python 3.12)
) else if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo Using venv
) else (
    echo ERROR: No virtual environment found!
    echo Please create .venv first using uv.
    pause
    exit /b 1
)

REM Load environment variables
if exist .env (
    echo Loading environment variables from .env
)

REM Suppress NumPy warnings
set PYTHONWARNINGS=ignore

REM Start FastAPI server
echo.
echo Starting server...
cd ..\.. && python backend/app.py
if errorlevel 1 (
    echo.
    echo ERROR: Backend failed to start!
    echo Check the error messages above.
    echo.
)

pause

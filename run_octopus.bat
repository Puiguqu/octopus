@echo off
echo Setting up and running Octopus automation script...
echo.

:: Get the directory where this batch file is located
set SCRIPT_DIR=%~dp0

:: Navigate to the script directory
cd /d "%SCRIPT_DIR%"

:: Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment. Make sure Python is installed and in PATH.
        pause
        exit /b 1
    )
    echo Virtual environment created successfully.
) else (
    echo Virtual environment already exists.
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment.
    pause
    exit /b 1
)

:: Check if requirements are already installed by looking for a key package
python -c "import cv2" 2>nul
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install requirements.
        pause
        exit /b 1
    )
    echo Packages installed successfully.
) else (
    echo Required packages are already installed.
)

:: Check if template images exist
if not exist "npc_gather.png" (
    echo WARNING: npc_gather.png not found!
)
if not exist "feed.png" (
    echo WARNING: feed.png not found!
)
if not exist "level7.png" (
    echo WARNING: level7.png not found!
)

echo.
echo Starting Octopus automation script...
echo Press Ctrl+C to stop the script.
echo.

:: Run the main script
python octopus.py

:: Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Script ended with an error.
    pause
)
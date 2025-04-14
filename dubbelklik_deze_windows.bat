@echo off
setlocal EnableDelayedExpansion

REM === Configuratie ===
set "REQUIRED_PYTHON=3.12"
set "PYTHON_EXEC=python%REQUIRED_PYTHON%"
set "VENV_DIR=venv"
set "PYTHON_SCRIPT=scripts\invoice_machine.py"
set "PYTHON_INSTALLER_SCRIPT=scripts\python_installer.bat"
set "DEPENDENCY_INSTALLER_SCRIPT=scripts\project_dependency_installer.bat"

REM === Stap 1: Zet werkdirectory op locatie van dit script ===
cd /d %~dp0
echo [INFO] Werkdirectory ingesteld op %cd%


REM === Stap 2: check voor python en run de python installer ===
where %PYTHON_EXEC% >nul 2>nul
if %errorlevel% equ 0 (
    echo [INFO] %PYTHON_EXEC% is al geïnstalleerd.

) else (
    echo [INFO] Start installatie van Python %REQUIRED_PYTHON%
    call %PYTHON_INSTALLER_SCRIPT%
)

REM === Stap 3: Check of venv beschikbaar is ===
python -m venv --help >nul 2>nul
if %errorlevel% equ 0 (
    echo [INFO] Venv is beschikbaak.
) else (
    echo [ERROR] Python venv-module ontbreekt. Installeer opnieuw met venv-optie.
    pause
    exit /b 1
)

REM === Stap 4: Virtuele omgeving aanmaken indien nodig ===
if not exist %VENV_DIR%\Scripts\activate.bat (
    echo [INFO] Virtuele omgeving wordt aangemaakt...
    %PYTHON_EXEC% -m venv %VENV_DIR%
)

REM === Stap 5: Activeer virtuele omgeving ===
call %VENV_DIR%\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Activatie van virtuele omgeving mislukt.
    pause
    exit /b 1
)
echo [INFO] Virtuele omgeving geactiveerd.

REM === Stap 6: Check of pip beschikbaar is ===
where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] pip is niet beschikbaar. Virtuele omgeving lijkt niet compleet.
    pause
    exit /b 1
)

REM === Stap 7: Installeer dependencies ===
set PYTHONPATH=%cd%
if exist requirements.txt (
    echo [INFO] Dependencies installeren vanuit requirements.txt...
    pip install --upgrade pip --quiet
    pip install -r requirements.txt --quiet
) else (
    echo [ERROR] Geen bestand met de naam 'requirements.txt' gevonden.
    pause
    exit /b 1
)

REM === Stap 8: Voer Python-script uit ===
echo [INFO] Druk op een toets om het script te starten.
pause
echo [INFO] Voer %PYTHON_SCRIPT% uit...
python %PYTHON_SCRIPT%

REM === Klaar ===
echo [INFO] Script uitgevoerd. Druk op een toets om af te sluiten...
pause
@echo off
setlocal EnableDelayedExpansion

REM === Configuratie ===
set "TARGET_DIR=libs"
set "REQUIREMENTS_FILE=requirements.txt"


REM === Stap 2: Controleer of requirements.txt bestaat ===
if not exist %REQUIREMENTS_FILE% (
    echo [WAARSCHUWING] %REQUIREMENTS_FILE% niet gevonden. Afbreken.
    pause
    exit /b 1
)

REM === Stap 3: Maak doelmap aan als die nog niet bestaat ===
if not exist %TARGET_DIR% (
    mkdir %TARGET_DIR%
)

REM === Stap 4: Installeer dependencies naar specifiek pad ===
echo [INFO] Installeer dependencies in map: %TARGET_DIR%
pip install --upgrade pip
pip install -r %REQUIREMENTS_FILE% --target=%TARGET_DIR%

if %errorlevel% equ 0 (
    echo [SUCCES] Dependencies succesvol geïnstalleerd in %TARGET_DIR%
) else (
    echo [FOUT] Installatie is mislukt. Controleer de foutmeldingen hierboven.
)

pause

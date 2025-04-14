@echo off
setlocal

REM === Configuratie ===
set "PYTHON_VERSION=3.12"
set "PYTHON_EXEC=python%PYTHON_VERSION%"
set "INSTALLER_NAME=python-%PYTHON_VERSION%-amd64.exe"
set "INSTALLER_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%INSTALLER_NAME%"

REM === Stap 1: Download installer als die nog niet lokaal staat ===
if not exist %INSTALLER_NAME% (
    echo [INFO] Python installer wordt gedownload...
    powershell -Command "Invoke-WebRequest -Uri '%INSTALLER_URL%' -OutFile '%INSTALLER_NAME%'"
    if %errorlevel% neq 0 (
        echo [ERROR] Download mislukt. Controleer internetverbinding of URL.
        exit /b 1
    )
)

REM === Stap 2: Voer de installer uit in stille modus ===
echo [INFO] Python wordt geïnstalleerd...
start /wait "" %INSTALLER_NAME% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
if %errorlevel% neq 0 (
    echo [ERROR] Python-installatie is mislukt.
    exit /b 1
)

REM === Stap 3: Controleer installatie ===
where %PYTHON_EXEC% >nul 2>nul
if %errorlevel% equ 0 (
    echo [SUCCES] Python %PYTHON_VERSION% is succesvol geïnstalleerd.
) else (
    echo [FOUT] Python is niet correct toegevoegd aan PATH. Herstart pc of voeg handmatig toe.
)

:einde
echo.
echo [INFO] Python Installer script voltooid.

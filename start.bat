@echo off
chcp 65001 >nul
title OmniAI - O'rnatish va ishga tushirish
color 0A

echo.
echo  ╔══════════════════════════════════════════╗
echo  ║       OmniAI - Ishga tushirish           ║
echo  ╚══════════════════════════════════════════╝
echo.

REM ─── Python tekshirish ───────────────────────────────────
echo [1/6] Python tekshirilmoqda...

py -3 --version >nul 2>&1
if %errorlevel% equ 0 (
    echo        [OK] Python (py launcher) topildi
    set PYTHON=py -3
    goto :check_venv
)

python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo        [OK] Python topildi
    set PYTHON=python
    goto :check_venv
)

python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    echo        [OK] Python3 topildi
    set PYTHON=python3
    goto :check_venv
)

REM Python topilmadi
echo.
echo  ╔══════════════════════════════════════════════════════╗
echo  ║  XATO: Python o'rnatilmagan!                        ║
echo  ║                                                      ║
echo  ║  Quyidagi qadamlarni bajaring:                      ║
echo  ║                                                      ║
echo  ║  1. https://www.python.org/downloads/ oching        ║
echo  ║  2. "Download Python 3.12" tugmasini bosing         ║
echo  ║  3. O'rnatishda:                                    ║
echo  ║     [*] "Add Python to PATH" ni ALBATTA belgilang!  ║
echo  ║  4. "Install Now" tugmasini bosing                  ║
echo  ║  5. O'rnatish tugagach kompyuterni qayta yuring     ║
echo  ║  6. Bu faylni yana ishga tushiring                  ║
echo  ╚══════════════════════════════════════════════════════╝
echo.
echo  Brauzerda python.org ochilmoqda...
start https://www.python.org/downloads/
echo.
pause
exit /b 1

:check_venv
REM ─── Virtual muhit ───────────────────────────────────────
echo.
echo [2/6] Virtual muhit tekshirilmoqda...

if not exist "venv\Scripts\activate.bat" (
    echo        Virtual muhit yaratilmoqda...
    %PYTHON% -m venv venv
    if %errorlevel% neq 0 (
        echo        [XATO] Virtual muhit yaratib bo'lmadi!
        pause
        exit /b 1
    )
    echo        [OK] Virtual muhit yaratildi
) else (
    echo        [OK] Virtual muhit mavjud
)

REM ─── Aktivlashtirish ─────────────────────────────────────
echo.
echo [3/6] Virtual muhit yoqilmoqda...
call venv\Scripts\activate.bat
echo        [OK] Faol

REM ─── Kutubxonalar ────────────────────────────────────────
echo.
echo [4/6] Kutubxonalar tekshirilmoqda...

pip show flask >nul 2>&1
if %errorlevel% neq 0 (
    echo        O'rnatilmoqda (2-4 daqiqa ketishi mumkin)...
    pip install -r requirements.txt --quiet
    if %errorlevel% neq 0 (
        echo        [XATO] Kutubxonalar o'rnatilmadi!
        echo        Internet aloqasini tekshiring va qayta urinib ko'ring.
        pause
        exit /b 1
    )
    echo        [OK] Barcha kutubxonalar o'rnatildi
) else (
    echo        [OK] Kutubxonalar mavjud
)

REM ─── Ma'lumotlar bazasi ───────────────────────────────────
echo.
echo [5/6] Ma'lumotlar bazasi sozlanmoqda...

if not exist "migrations\env.py" (
    echo        Flask-Migrate ishga tushirilmoqda...
    flask db init >nul 2>&1
)

flask db migrate -m "Jadvallar" >nul 2>&1
flask db upgrade
if %errorlevel% neq 0 (
    echo        [XATO] Baza sozlanmadi! Xatoni tekshiring.
    pause
    exit /b 1
)
echo        [OK] Ma'lumotlar bazasi tayyor

REM ─── Ishga tushirish ─────────────────────────────────────
echo.
echo [6/6] OmniAI ishga tushirilmoqda...
echo.
echo  ╔══════════════════════════════════════════════════╗
echo  ║                                                  ║
echo  ║   OmniAI ISHGA TUSHDI!                          ║
echo  ║                                                  ║
echo  ║   Brauzerda oching:                             ║
echo  ║   http://localhost:5000                         ║
echo  ║                                                  ║
echo  ║   To'xtatish uchun: Ctrl+C                      ║
echo  ║                                                  ║
echo  ╚══════════════════════════════════════════════════╝
echo.

REM Brauzer avtomatik ochish (3 soniya kechikish bilan)
timeout /t 3 /nobreak >nul
start http://localhost:5000

REM Flask ilovasini ishga tushirish
python run.py

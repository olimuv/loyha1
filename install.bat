@echo off
echo ============================================
echo   OmniAI - O'rnatish skripti
echo ============================================
echo.

REM Python mavjudligini tekshirish
python --version 2>nul
if %errorlevel% neq 0 (
    echo [XATO] Python o'rnatilmagan!
    echo.
    echo Python o'rnatish uchun:
    echo 1. https://www.python.org/downloads/ saytiga o'ting
    echo 2. Python 3.11 yoki undan yangi versiyasini yuklab oling
    echo 3. O'rnatishda "Add Python to PATH" katagiga belgi qo'ying!
    echo 4. Kompyuterni qayta yuring
    echo 5. Bu faylni yana ishga tushiring
    pause
    exit /b 1
)

echo [OK] Python topildi
echo.

REM Virtual muhit yaratish
if not exist "venv" (
    echo Virtual muhit yaratilmoqda...
    python -m venv venv
    echo [OK] Virtual muhit yaratildi
) else (
    echo [OK] Virtual muhit allaqachon mavjud
)

echo.
echo Virtual muhitni yoqish...
call venv\Scripts\activate.bat

echo.
echo Kutubxonalar o'rnatilmoqda (bir necha daqiqa ketishi mumkin)...
pip install -r requirements.txt

echo.
echo Ma'lumotlar bazasi sozlanmoqda...
flask db init 2>nul
flask db migrate -m "Dastlabki jadvallar" 2>nul
flask db upgrade

echo.
echo ============================================
echo   O'rnatish tugadi!
echo ============================================
echo.
echo Ilovani ishga tushirish uchun:
echo   python run.py
echo.
echo Brauzerda oching:
echo   http://localhost:5000
echo.
pause

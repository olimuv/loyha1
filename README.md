# OmniAI — AI Customer Support Platform

O'zbekiston bozori uchun yaratilgan AI mijozlar xizmati SaaS platformasi.

## Texnologiyalar
- **Backend:** Python, Flask, SQLAlchemy, Flask-Login
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Frontend:** HTML5, CSS3, Vanilla JS, Chart.js
- **AI:** OpenAI GPT-3.5 (API kaliti bo'lmasa fallback rejimi)

## Tezkor o'rnatish (Windows 10)

### 1. Python o'rnatish
[python.org](https://www.python.org/downloads/) dan Python 3.11+ yuklab o'rnatish.
O'rnatishda **"Add Python to PATH"** katagiga belgi qo'ying!

### 2. Virtual muhit yaratish va ishga tushirish
```powershell
cd D:\LOYHA\OmniAI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Ma'lumotlar bazasini ishga tushirish
```powershell
flask db init
flask db migrate -m "Dastlabki migratsiya"
flask db upgrade
```

### 4. Ilovani ishga tushirish
```powershell
python run.py
```
Brauzerda oching: `http://localhost:5000`

### 5. Testlarni ishga tushirish
```powershell
pytest tests/ -v
```

## AI sozlash (ixtiyoriy)
`.env` faylida `OPENAI_API_KEY=` ga kalitingizni kiriting.
API kaliti bo'lmasa tizim **fallback** rejimda ishlaydi — bu haqda foydalanuvchiga xabar beriladi.

## Xavfsizlik eslatmalari
- `.env` faylini hech qachon Git'ga qo'shmang
- Production'da `SECRET_KEY` ni o'zgartiring (kamida 32 belgi)
- Production'da `FLASK_DEBUG=False` qiling
- Production'da PostgreSQL ishlating

## Loyiha tuzilishi
```
OmniAI/
├── run.py              # Ishga tushirish
├── config.py           # Konfiguratsiya
├── requirements.txt    # Kutubxonalar
├── .env                # Maxfiy sozlamalar (Git'ga qo'shilmaydi)
├── app/
│   ├── __init__.py     # App factory
│   ├── extensions.py   # Flask kengaytmalari
│   ├── models/         # DB modellari
│   ├── auth/           # Login/Register
│   ├── dashboard/      # Asosiy boshqaruv
│   ├── knowledge/      # Bilimlar bazasi
│   ├── conversations/  # Suhbatlar
│   ├── analytics/      # Analitika
│   ├── settings/       # Sozlamalar
│   ├── api/            # REST API
│   ├── services/       # AI xizmati
│   ├── templates/      # HTML shablonlar
│   └── static/         # CSS, JS, rasmlar
└── tests/              # Testlar
```

## Muammolarni hal qilish

**"python" topilmadi xatosi:**
`python` o'rniga `python3` yozing, yoki Python'ni qayta o'rnating.

**"pip" topilmadi:**
```powershell
python -m pip install -r requirements.txt
```

**Port 5000 band:**
```powershell
# run.py da port=5001 qilib o'zgartiring
```

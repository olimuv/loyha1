"""
OmniAI - Ilovani ishga tushirish fayli
Foydalanish: python run.py
"""

import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    print("=" * 60, flush=True)
    print("  OmniAI ishga tushmoqda...", flush=True)
    print(f"  Muhit: {os.environ.get('FLASK_ENV', 'development')}", flush=True)
    print(f"  Debug: {debug_mode}", flush=True)
    port = int(os.environ.get('PORT', 5050))
    print(f"  URL: http://localhost:{port}", flush=True)
    print("=" * 60, flush=True)
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug_mode,
        use_reloader=False
    )



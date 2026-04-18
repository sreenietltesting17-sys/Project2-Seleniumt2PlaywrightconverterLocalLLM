import os
import uuid
import datetime

TMP_DIR = ".tmp"
DELIVERY_DIR = "delivery"

def ensure_directories():
    os.makedirs(TMP_DIR, exist_ok=True)
    os.makedirs(DELIVERY_DIR, exist_ok=True)

def save_converted_file(code: str, target_lang: str) -> str:
    """
    Saves the produced code to .tmp and copy to delivery folder, returning the delivery path.
    """
    ensure_directories()
    
    ext = "ts" if target_lang.lower() == "typescript" else "js"
    filename = f"playwright_test_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:6]}.{ext}"
    
    tmp_path = os.path.join(TMP_DIR, filename)
    delivery_path = os.path.join(DELIVERY_DIR, filename)
    
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(code)
        
    with open(delivery_path, "w", encoding="utf-8") as f:
        f.write(code)
        
    # Return absolute path conceptually, but relative is fine for UI
    return os.path.abspath(delivery_path)

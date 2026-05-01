import os
from PIL import Image

def get_data():
    return {"LAST_SPRITE": "None", "SPRITE_STATUS": "Ready"}

def load_sprite(path):
    """Проверяет файл и возвращает его параметры"""
    if os.path.exists(path):
        try:
            with Image.open(path) as img:
                w, h = img.size
                fmt = img.format
            return {
                "SPRITE_PATH": path,
                "SPRITE_W": str(w),
                "SPRITE_H": str(h),
                "SPRITE_FORMAT": fmt,
                "SPRITE_STATUS": "Loaded"
            }
        except:
            return {"SPRITE_STATUS": "Error: Invalid Image"}
    return {"SPRITE_STATUS": "Error: File Not Found"}
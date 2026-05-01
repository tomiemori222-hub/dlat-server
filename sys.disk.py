import shutil
import os

def get_data():
    """Получает данные о диске C в стиле проводника Windows"""
    try:
        # Получаем данные в байтах
        total, used, free = shutil.disk_usage("C:\\")
        
        # Переводим в Гигабайты (делим на 1024^3)
        total_gb = total / (1024**3)
        free_gb = free / (1024**3)
        
        # Считаем занятое место ТАК ЖЕ, как Windows (Общее - Свободное)
        real_used_gb = total_gb - free_gb
        
        return {
            "USED": str(round(real_used_gb, 1)), # Занято
            "FREE": str(round(free_gb, 1)),      # Свободно
            "TOTAL": str(round(total_gb, 1))     # Всего
        }
    except Exception as e:
        return {"USED": "0", "FREE": "0", "TOTAL": "0"}
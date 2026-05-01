# DLL++ Library: sys.disk
import shutil
import os

def get_disk_info(drive="C:\\"):
    total, used, free = shutil.disk_usage(drive)
    return {
        "total": round(total / (2**30), 2),
        "used": round(used / (2**30), 2),
        "free": round(free / (2**30), 2),
        "percent": round((used / total) * 100, 1)
    }

def find_biggest_file(path="C:\\"):
    """Ищет самый большой файл в указанной директории (не заходя глубоко в системные папки)"""
    max_size = 0
    biggest_file = ""
    
    try:
        # Проверяем только корень и первый уровень папок для скорости
        for entry in os.scandir(path):
            if entry.is_file():
                size = entry.stat().st_size
                if size > max_size:
                    max_size = size
                    biggest_file = entry.path
    except Exception:
        return "Доступ ограничен", 0
        
    return biggest_file, round(max_size / (2**20), 2) # Возвращаем путь и размер в МБ
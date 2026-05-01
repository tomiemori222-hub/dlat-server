import shutil
import os

def get_stats(drive="C:\\"):
    total, used, free = shutil.disk_usage(drive)
    return {
        "used": round(used / (2**30), 2),
        "free": round(free / (2**30), 2)
    }

def get_biggest(path="C:\\"):
    # Простой поиск в корне для примера
    files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if not files: return "None", 0
    biggest = max(files, key=os.path.getsize)
    return os.path.basename(biggest), round(os.path.getsize(biggest) / (2**20), 2)
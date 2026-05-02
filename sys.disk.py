"""DLL++ System Disk - информация о дисках"""
import shutil, platform

def disk_usage(path="C:\\"):
    if platform.system() == "Windows":
        total, used, free = shutil.disk_usage(path)
        return {"total_gb": round(total/1024**3, 2),
                "used_gb": round(used/1024**3, 2),
                "free_gb": round(free/1024**3, 2)}
    else:
        # для unix
        total, used, free = shutil.disk_usage("/")
        return {"total_gb": round(total/1024**3, 2),
                "used_gb": round(used/1024**3, 2),
                "free_gb": round(free/1024**3, 2)}

def execute(cmd):
    """
    cmd: буква диска (C:\) или пусто (системный)
    """
    drive = cmd.strip() if cmd.strip() else "C:\\"
    info = disk_usage(drive)
    print(f"[disk] Диск {drive}: Занято {info['used_gb']} ГБ, Свободно {info['free_gb']} ГБ")
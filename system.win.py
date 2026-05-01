import os, platform, subprocess, time

def get_data():
    try:
        # Получаем время работы ПК (uptime)
        uptime_seconds = time.time() - psutil_boot_time() if 'psutil' in sys.modules else 0
        
        return {
            "USER": os.getlogin(),
            "PC_NAME": platform.node(),
            "OS_FULL": f"{platform.system()} {platform.release()}",
            "CPU": platform.processor(),
            "ARCH": platform.machine(),
            "VER": platform.version()
        }
    except:
        return {"USER": os.getlogin(), "OS_FULL": "Windows"}
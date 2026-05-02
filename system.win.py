"""DLL++ System Info - информация о Windows"""
import platform, os, time, socket

def get_data():
    return {
        "OS": platform.system(),
        "OS_FULL": platform.platform(),
        "USER": os.getlogin(),
        "COMPUTER": socket.gethostname(),
        "UPTIME": time.time() - psutil.boot_time() if 'psutil' in globals() else "?",
        "PYTHON": platform.python_version()
    }

def execute(cmd):
    """
    cmd: full - полная информация, либо пусто - кратко
    """
    info = get_data()
    if cmd == "full":
        for k, v in info.items():
            print(f"  {k}: {v}")
    else:
        print(f"[sys] ОС: {info['OS_FULL']}, Пользователь: {info['USER']}, Компьютер: {info['COMPUTER']}")
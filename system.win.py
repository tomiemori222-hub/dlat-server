# DLL++ System Library: system.win
import os
import subprocess

def get_data():
    """Получает имя пользователя и версию Windows"""
    import platform
    return {
        "USER": os.getlogin(),
        "OS_VER": platform.release(),
        "ARCH": platform.machine()
    }

def action(cmd):
    """Выполняет системные действия"""
    if cmd == "shutdown":
        os.system("shutdown /s /t 1")
    elif cmd == "restart":
        os.system("shutdown /r /t 1")
    elif cmd == "lock":
        import ctypes
        ctypes.windll.user32.LockWorkStation()

def process_kill(name):
    """Принудительно завершает процесс"""
    os.system(f"taskkill /f /im {name}")
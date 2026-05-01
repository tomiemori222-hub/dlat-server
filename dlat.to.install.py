# DLL++ Library: dlat.to.exe
import os
import subprocess

def compile_to_exe(script_name):
    """Превращает скрипт dlat/py в готовый EXE файл"""
    if not os.path.exists(script_name):
        print(f"[-] Ошибка: Файл {script_name} не найден.")
        return

    print(f"[*] Начинаю сборку EXE из {script_name}...")
    print("[*] Это может занять пару минут...")

    # Команда для компиляции через PyInstaller
    # --onefile делает один EXE, --noconsole убирает черное окно
    cmd = f"pyinstaller --onefile --noconsole {script_name}"
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Сборка завершена! Ищи файл в папке /dist")
    except Exception as e:
        print(f"[-] Ошибка сборки: {e}")

# Команда: dll}bat{=dlat.to.exe(build):myscript.py:
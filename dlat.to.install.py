# DLL++ System Library: dlat.to.install
import os
import subprocess
import sys

def build_exe(dlat_file, modules_path):
    """Процесс превращения dlat скрипта в независимый EXE"""
    if not os.path.exists(dlat_file):
        return False
    
    name = os.path.splitext(dlat_file)[0]
    py_file = name + ".py"
    
    # Создаем временный файл Python
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write("import os, sys\n")
        f.write(f"sys.path.append(r'{modules_path}')\n")
        # Здесь будет код, который импортирует ядро и запускает файл
        f.write(f"print('Running DLL++ System Project...')\n")
    
    # Запуск PyInstaller
    try:
        subprocess.run(f"pyinstaller --onefile --noconsole {py_file}", shell=True)
        if os.path.exists(py_file): os.remove(py_file)
        return True
    except:
        return False
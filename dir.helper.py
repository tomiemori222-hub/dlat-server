# DLL++ Library: dir.helper
import os

def scan_system(path="C:\\"):
    """Сканирует папку и ищет подозрительные файлы"""
    suspicious_files = []
    print(f"[*] Сканирование {path} на угрозы...")
    for root, dirs, files in os.walk(path):
        for file in files:
            # Например, ищем файлы с двойным расширением (признак вируса)
            if file.count('.') > 1 and file.endswith('.exe'):
                suspicious_files.append(os.path.join(root, file))
    return suspicious_files

def get_tree(path):
    """Показывает все папки в директории"""
    return os.listdir(path)

# Команда: dll}bat{=dir.helper(scan):C:\Users\Downloads:
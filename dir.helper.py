"""DLL++ Dir Helper - сканирование папок"""
import os

def scan(path):
    try:
        items = os.listdir(path)
        return items
    except:
        return []

def execute(cmd):
    """
    cmd: путь к папке (или пусто = рабочий стол)
    Выводит список файлов и папок в консоль DLL++
    """
    target = cmd.strip() if cmd.strip() else os.path.expanduser("~/Desktop")
    items = scan(target)
    print(f"[dir] Содержимое {target}:")
    for item in items:
        print(f"  {item}")
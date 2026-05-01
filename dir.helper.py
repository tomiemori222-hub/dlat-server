# DLL++ System Library: dir.helper
import os
import shutil

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return f"Папка {path} создана"
    return "Папка уже существует"

def delete_anything(path):
    """Удаляет файл или папку со всем содержимым"""
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)

def list_files(path="."):
    """Возвращает список всех файлов в папке для STORAGE"""
    files = ", ".join(os.listdir(path))
    return {"FILE_LIST": files}
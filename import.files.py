"""DLL++ Import.Files - загрузка содержимого файлов для обучения кода 19"""
import os

TRAINING_STORAGE = {}  # Словарь, в котором обученные тексты (имя файла -> содержимое)

def read_file(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def execute(cmd):
    """
    Команда: <путь к файлу>
    Загружает файл и помещает его содержимое в глобальное хранилище TRAINING_STORAGE.
    Доступно для кода 19 через ключ 'learned_data'.
    """
    path = cmd.strip()
    if not path:
        print("[import.files] Укажите путь к файлу.")
        return
    data = read_file(path)
    if data is None:
        print(f"[import.files] Файл не найден: {path}")
        return
    TRAINING_STORAGE[os.path.basename(path)] = data
    print(f"[import.files] Загружено: {path} ({len(data)} символов)")
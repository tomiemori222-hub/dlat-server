"""DLL++ Storage - сохранение/загрузка переменных в JSON"""
import json, os

STORAGE_FILE = "dll_storage.json"

def save(data):
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[storage] Данные сохранены в {STORAGE_FILE}")

def load():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def execute(cmd):
    """
    Команды: save (сохраняет текущий STORAGE движка), load (загружает и выводит)
    Для работы необходимо передавать сам STORAGE из движка (сделаем через глобальные переменные)
    """
    # Мы можем обратиться к STORAGE напрямую, если движок импортирует этот модуль
    # Но проще - движок сам вызовет save с аргументом. Пока упростим: команда save ничего не делает без данных.
    if cmd == "save":
        print("[storage] Для сохранения нужно вызвать из движка передачу STORAGE")
    elif cmd == "load":
        data = load()
        print("[storage] Загруженные данные:", data)
    else:
        print("[storage] Команды: save, load")
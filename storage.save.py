"""
DLL++ Storage Library - сохраняет/загружает переменные STORAGE в/из JSON.
"""

import json, os

DEFAULT_FILE = "dll_storage.json"

def execute(cmd):
    # Получаем переданные объекты (если были)
    from sys import modules
    mod = modules.get("storage.save")
    if not mod or not hasattr(mod, "storage"):
        print("[storage] Ошибка: нет связи с движком. Загрузите библиотеку корректно.")
        return
    STORAGE = mod.storage
    REGISTRY = getattr(mod, "registry", {})

    if cmd == "save":
        data = {"storage": dict(STORAGE), "registry": dict(REGISTRY), "version": "1.0"}
        with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[storage] Данные сохранены в {DEFAULT_FILE}")
    elif cmd == "load":
        if not os.path.exists(DEFAULT_FILE):
            print("[storage] Файл сохранения не найден.")
            return
        with open(DEFAULT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        STORAGE.clear()
        STORAGE.update(data.get("storage", {}))
        REGISTRY.clear()
        REGISTRY.update(data.get("registry", {}))
        print("[storage] Данные загружены.")
    elif cmd == "clear":
        if os.path.exists(DEFAULT_FILE):
            os.remove(DEFAULT_FILE)
        STORAGE.clear()
        REGISTRY.clear()
        print("[storage] Хранилище очищено (файл удалён).")
    else:
        print("[storage] Команды: save, load, clear")

def initialize(storage, registry=None):
    import sys
    mod = sys.modules.get("storage.save")
    if mod:
        mod.storage = storage
        mod.registry = registry or {}

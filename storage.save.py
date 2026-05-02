"""DLL++ Storage - сохранение/загрузка переменных STORAGE"""
import json, os, sys

DEFAULT_FILE = "dll_storage.json"

def execute(cmd):
    # Берём storage/registry из атрибутов модуля (установлены движком)
    mod = sys.modules[__name__]
    storage = getattr(mod, 'storage', {})
    registry = getattr(mod, 'registry', {})

    if cmd == "save":
        data = {"storage": dict(storage), "registry": dict(registry), "version": "1.0"}
        with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[storage] Данные сохранены в {DEFAULT_FILE}")
    elif cmd == "load":
        if not os.path.exists(DEFAULT_FILE):
            print("[storage] Файл сохранения не найден.")
            return
        with open(DEFAULT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        storage.clear()
        storage.update(data.get("storage", {}))
        registry.clear()
        registry.update(data.get("registry", {}))
        print("[storage] Данные загружены.")
    elif cmd == "clear":
        if os.path.exists(DEFAULT_FILE):
            os.remove(DEFAULT_FILE)
        storage.clear()
        registry.clear()
        print("[storage] Хранилище очищено.")
    else:
        print("[storage] Команды: save, load, clear")

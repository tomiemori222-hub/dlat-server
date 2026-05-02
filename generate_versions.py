import hashlib, json, os

LIB_DIR = "."   # папка, где лежат .py файлы библиотек (обычно корень репозитория)
VERSION_FILE = "versions.json"

def md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

versions = {}
for fname in os.listdir(LIB_DIR):
    if fname.endswith(".py") and fname not in ("generate_versions.py", "dlat.py"):
        versions[fname] = md5(os.path.join(LIB_DIR, fname))

with open(VERSION_FILE, "w", encoding="utf-8") as f:
    json.dump(versions, f, indent=4)

print(f"Готово! Хеши {len(versions)} библиотек записаны в {VERSION_FILE}")
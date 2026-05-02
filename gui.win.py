"""DLL++ HTTP Installer - скачивание файлов по URL"""
import urllib.request, os

def download(url, save_as=None):
    try:
        if not save_as:
            save_as = url.split("/")[-1] or "downloaded_file"
        urllib.request.urlretrieve(url, save_as)
        print(f"[http] Файл сохранён: {save_as}")
    except Exception as e:
        print(f"[http] Ошибка загрузки: {e}")

def execute(cmd):
    """
    Формат: url;имя_файла (имя файла необязательно)
    """
    parts = cmd.split(";")
    url = parts[0].strip()
    name = parts[1].strip() if len(parts) > 1 else None
    download(url, name)
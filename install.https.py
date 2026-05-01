# DLL++ Library: install.url
import urllib.request
import os

def download_media(url, filename):
    try:
        ext = url.split('.')[-1]
        full_name = f"{filename}.{ext}"
        print(f"[*] Скачивание файла {full_name}...")
        urllib.request.urlretrieve(url, full_name)
        print(f"[+] Файл сохранен: {os.path.abspath(full_name)}")
    except Exception as e:
        print(f"[-] Ошибка загрузки: {e}")

# Команда: dll}bat{=install.url(get):https://site.com/image.png,my_art:
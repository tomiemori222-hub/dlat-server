"""DLL++ Sprite Import - загрузка изображений в canvas (через библиотеку draw.canvas)"""
import importlib, os
from tkinter import PhotoImage

def execute(cmd):
    """
    cmd: путь_к_изображению
    Загружает изображение и выводит в окне Canvas (через draw.canvas)
    """
    path = cmd.strip()
    if not os.path.exists(path):
        print(f"[sprite] Файл не найден: {path}")
        return
    # Используем draw.canvas для отображения
    if "draw.canvas" in sys.modules:
        mod = sys.modules["draw.canvas"]
        from threading import Thread
        win = mod.DrawingWindow(400, 400, "Sprite")
        img = PhotoImage(file=path)
        win.canvas.create_image(200, 200, image=img)
        win.canvas.image = img  # сохранить ссылку
        Thread(target=win.show, daemon=True).start()
    else:
        print("[sprite] Необходима загруженная библиотека draw.canvas")
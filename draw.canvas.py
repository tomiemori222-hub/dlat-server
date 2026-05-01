# DLL++ Multimedia Library: draw.canvas
from tkinter import Tk, Canvas, BOTH
from PIL import Image, ImageDraw

def create_window(w, h, title="DLL++ Canvas"):
    """Создает окно для рисования"""
    root = Tk()
    root.title(title)
    canvas = Canvas(root, width=w, height=h, bg="white")
    canvas.pack(fill=BOTH, expand=True)
    return root, canvas

def get_data():
    """Возвращает параметры экрана для системы"""
    from tkinter import Tk
    root = Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.destroy()
    return {"SCREEN_W": str(w), "SCREEN_H": str(h)}

def save_canvas(commands, filename="output.png"):
    """Генерирует изображение на основе команд dlat и сохраняет его"""
    img = Image.new("RGB", (800, 600), "white")
    draw = ImageDraw.Draw(img)
    # Пример логики: обработка простых команд рисования
    for cmd in commands:
        if "rect" in cmd:
            draw.rectangle([10, 10, 100, 100], fill="red")
    img.save(filename)
    return f"Saved to {filename}"
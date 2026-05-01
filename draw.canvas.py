# DLL++ Library: draw.canvas
import tkinter as tk

def create_window(title="DLL++ Canvas", width=800, height=600):
    root = tk.Tk()
    root.title(title)
    canvas = tk.Canvas(root, width=width, height=height, bg="black")
    canvas.pack()
    print(f"[Canvas] Окно {width}x{height} создано.")
    return root, canvas

def draw_rect(canvas, x, y, w, h, color):
    return canvas.create_rectangle(x, y, x+w, y+h, fill=color, outline="")

# Команда для вызова из DLL++: dll}bat{=draw.canvas(rect):0,0,50,50,red:
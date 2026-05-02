"""DLL++ 2D Canvas - рисование фигур и спрайтов"""
from tkinter import Tk, Canvas
from threading import Thread

class DrawingWindow:
    def __init__(self, width=400, height=300, title="DLL++ Canvas"):
        self.root = Tk()
        self.root.title(title)
        self.canvas = Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
    def line(self, x1, y1, x2, y2, fill="black"):
        self.canvas.create_line(x1, y1, x2, y2, fill=fill)
    def oval(self, x1, y1, x2, y2, fill="gray"):
        self.canvas.create_oval(x1, y1, x2, y2, fill=fill)
    def show(self):
        self.root.mainloop()

def execute(cmd):
    """
    cmd: JSON с командами рисования.
    Пример: {"width":400,"height":300,"commands":[["line",10,10,100,100,"red"],["oval",50,50,150,150,"blue"]]}
    """
    import json
    try:
        data = json.loads(cmd)
    except:
        print("[canvas] Неверный JSON")
        return
    w, h = data.get("width", 400), data.get("height", 300)
    win = DrawingWindow(w, h, data.get("title", "Canvas"))
    for cmd in data.get("commands", []):
        if cmd[0] == "line":
            win.line(*cmd[1:])
        elif cmd[0] == "oval":
            win.oval(*cmd[1:])
        # можно расширить
    Thread(target=win.show, daemon=True).start()
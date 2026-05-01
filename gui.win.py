from tkinter import messagebox, Tk

def show(title, text):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, text)
    root.destroy()
# DLL++ Library: gui.win
from tkinter import messagebox

def show_message(title, text):
    messagebox.showinfo(title, text)

def show_error(title, text):
    messagebox.showerror(title, text)

def ask_question(title, text):
    return messagebox.askyesno(title, text)

# Команда для вызова из DLL++: dll}bat{=gui.win(msg):Внимание,Система готова!:
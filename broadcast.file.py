"""DLL++ Broadcast - запись логов в файл с временной меткой"""
import datetime

def log(message, filename="dll_broadcast.log"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")

def execute(cmd):
    """
    Формат: имя_файла:сообщение
    Если имя файла не указано, пишет в dll_broadcast.log
    """
    if ":" in cmd:
        fname, msg = cmd.split(":", 1)
        log(msg, fname.strip())
    else:
        log(cmd)
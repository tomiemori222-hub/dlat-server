# DLL++ Library: broadcast.file
import datetime

def send_message(target_file, message):
    """Записывает сообщение в файл с меткой времени"""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    with open(target_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] DLL++ Message: {message}\n")
    print(f"[+] Сообщение отправлено в {target_file}")

# Команда: dll}bat{=broadcast.file(send):log.txt,Система запущена успешно:
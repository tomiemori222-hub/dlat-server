# DLL++ Multimedia Library: audio.work
import os
import subprocess

def get_data():
    """Данные об аудио-устройствах"""
    return {"AUDIO_DRIVER": "DirectSound/Windows"}

def speak(text):
    """Озвучивает текст голосом Windows (SAPI)"""
    # Создаем временный скрипт VBS для озвучки без сторонних библиотек
    vbs_code = f'Set sapi=CreateObject("sapi.spvoice"):sapi.Speak "{text}"'
    with open("temp_voice.vbs", "w", encoding="cp1251") as f:
        f.write(vbs_code)
    os.system("cscript //nologo temp_voice.vbs")
    os.remove("temp_voice.vbs")

def play_system_sound(type="info"):
    """Играет системные звуки Windows"""
    import ctypes
    sounds = {"info": 64, "error": 16, "warn": 48, "ok": 32}
    ctypes.windll.user32.MessageBeep(sounds.get(type, 64))

def beep(freq, duration):
    """Пищит спикером (частота, длительность)"""
    import winsound
    winsound.Beep(int(freq), int(duration))
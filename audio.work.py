# DLL++ Library: audio.work
import winsound
import os

def play_system_sound(sound_type):
    # sound_type: 'error', 'ok', 'question'
    if sound_type == 'error':
        winsound.MessageBeep(winsound.MB_ICONHAND)
    elif sound_type == 'ok':
        winsound.MessageBeep(winsound.MB_OK)

def play_file(file_path):
    if os.path.exists(file_path):
        # Используем стандартный плеер Windows или библиотеку
        os.startfile(file_path)
    else:
        print(f"[Audio Error] Файл {file_path} не найден.")

# Команда для вызова из DLL++: dll}bat{=audio.work(play):music.mp3:
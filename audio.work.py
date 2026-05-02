"""DLL++ Audio Library - TTS и системные звуки"""
import subprocess, platform, threading
try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    TTS = True
except:
    TTS = False

def speak(text):
    if TTS:
        def _run():
            engine.say(text)
            engine.runAndWait()
        threading.Thread(target=_run, daemon=True).start()
    else:
        print("[audio] pyttsx3 не установлен")

def play_system_sound(sound="Asterisk"):
    if platform.system() == "Windows":
        import winsound
        sounds = {"Asterisk": winsound.MB_ICONASTERISK, "Exclamation": winsound.MB_ICONEXCLAMATION,
                  "Critical": winsound.MB_ICONHAND, "Question": winsound.MB_ICONQUESTION}
        winsound.MessageBeep(sounds.get(sound, winsound.MB_OK))
    else:
        print("[audio] Системные звуки только для Windows")

def execute(cmd):
    """
    Команды:
        say:Привет          - произнести текст
        beep:Critical       - системный звук (Asterisk/Exclamation/Critical/Question)
    """
    if cmd.startswith("say:"):
        speak(cmd[4:])
    elif cmd.startswith("beep:"):
        play_system_sound(cmd[5:])
    else:
        speak(cmd)  # по умолчанию говорить
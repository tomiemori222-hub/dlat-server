"""DLL++ Security Scan - процессы и отладка"""
import psutil, sys

def list_processes():
    procs = [p.info for p in psutil.process_iter(['pid', 'name'])]
    return procs[:20]  # ограничим вывод

def check_debug():
    # простая проверка, запущен ли отладчик (только для Windows)
    if sys.gettrace() is not None:
        return True
    return False

def execute(cmd):
    """
    cmd: proc - показать процессы, debug - проверка отладчика
    """
    if cmd == "proc":
        procs = list_processes()
        print("[sec] Активные процессы:")
        for p in procs:
            print(f"  PID {p['pid']}: {p['name']}")
    elif cmd == "debug":
        if check_debug():
            print("[sec] ВНИМАНИЕ: обнаружен отладчик!")
        else:
            print("[sec] Отладчик не активен")
    else:
        print("[sec] Команды: proc, debug")
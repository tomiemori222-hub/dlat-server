import subprocess

def get_data():
    try:
        # Получаем список процессов через tasklist
        output = subprocess.check_output('tasklist', shell=True).decode('cp866')
        lines = output.split('\n')
        proc_count = len(lines) - 3 # Вычитаем заголовок
        
        # Проверка на наличие инструментов отладки
        tools = ["taskmgr.exe", "processhacker.exe", "wireshark.exe", "cmd.exe"]
        found = [p for p in tools if p in output.lower()]
        
        return {
            "PROC_COUNT": str(proc_count),
            "THREATS": "Clean" if not found else f"Detected ({len(found)})",
            "TOOL_LIST": ", ".join(found) if found else "None"
        }
    except:
        return {"PROC_COUNT": "0", "THREATS": "Error"}
# DLL++ System Library: security.scan
import os
import subprocess

def get_data():
    """Ищет подозрительные процессы (например, мониторы ресурсов)"""
    suspicious = ["taskmgr.exe", "processhacker.exe", "wireshark.exe"]
    found = []
    
    # Получаем список запущенных процессов через tasklist
    output = subprocess.check_output('tasklist', shell=True).decode('cp866').lower()
    
    for p in suspicious:
        if p in output:
            found.append(p)
            
    return {
        "THREATS_COUNT": str(len(found)),
        "THREAT_LIST": ", ".join(found) if found else "None"
    }
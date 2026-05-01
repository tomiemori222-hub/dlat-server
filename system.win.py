# DLL++ Library: system.win
import os
import subprocess

def run_cmd(command):
    """Запуск любой команды в скрытом режиме"""
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def lock_pc():
    """Заблокировать компьютер"""
    os.system("rundll32.exe user32.dll,LockWorkStation")

def restart_explorer():
    """Перезапустить проводник (если завис)"""
    os.system("taskkill /f /im explorer.exe && start explorer.exe")

# Команда: dll}bat{=system.win(lock):
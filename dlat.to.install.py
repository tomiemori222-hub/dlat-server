"""DLL++ Converter - упаковка .dlat в исполняемый файл (PyInstaller)"""
import os, sys

def convert(script_path, output_exe=None):
    try:
        import PyInstaller.__main__ as pyi
    except ImportError:
        print("[installer] Установите PyInstaller: pip install pyinstaller")
        return
    if not os.path.exists(script_path):
        print(f"[installer] Файл {script_path} не найден")
        return
    args = ["--onefile", script_path]
    if output_exe:
        args += ["-n", output_exe]
    pyi.run(args)

def execute(cmd):
    """
    cmd: путь_к_скрипту.dlat
    Конвертирует скрипт в .exe (осторожно, требует PyInstaller)
    """
    script = cmd.strip()
    if script:
        convert(script)
    else:
        print("[installer] Укажите путь к .dlat файлу")
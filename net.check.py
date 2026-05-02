"""DLL++ Network Check - внешний IP и пинг"""
import urllib.request, json

def get_ext_ip():
    try:
        return urllib.request.urlopen("https://api.ipify.org?format=json").read().decode()
    except:
        return '{"ip":"недоступен"}'

def ping(host):
    import subprocess, platform
    param = "-n" if platform.system().lower()=="windows" else "-c"
    cmd = ["ping", param, "1", host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def execute(cmd):
    """
    Команды: ip, ping:адрес
    """
    if cmd == "ip":
        data = json.loads(get_ext_ip())
        print(f"[net] Внешний IP: {data.get('ip')}")
    elif cmd.startswith("ping:"):
        host = cmd.split(":",1)[1]
        print(ping(host))
    else:
        print("[net] Используйте: ip или ping:хост")
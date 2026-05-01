import socket, urllib.request, subprocess

def get_data():
    try:
        # Проверка внешнего IP
        ext_ip = urllib.request.urlopen('https://api.ipify.org', timeout=3).read().decode('utf8')
        
        # Проверка пинга до Google
        ping_res = subprocess.run(['ping', '-n', '1', '8.8.8.8'], capture_output=True, text=True)
        ping = "OK" if ping_res.returncode == 0 else "High Latency"
        
        return {
            "LOCAL_IP": socket.gethostbyname(socket.gethostname()),
            "EXT_IP": ext_ip,
            "NET_STATUS": "Connected",
            "PING": ping
        }
    except:
        return {"NET_STATUS": "Offline", "EXT_IP": "None", "PING": "Error"}
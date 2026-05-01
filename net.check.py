# DLL++ System Library: net.check
import socket
import urllib.request

def get_data():
    """Проверяет соединение и получает IP"""
    try:
        # Получаем локальный IP
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        # Проверяем интернет (Google DNS)
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        status = "Online"
        
        # Получаем внешний IP (через API)
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    except:
        status = "Offline"
        local_ip = "127.0.0.1"
        external_ip = "None"

    return {
        "NET_STATUS": status,
        "LOCAL_IP": local_ip,
        "EXT_IP": external_ip
    }
import socket
import os,time,json,requests
import datetime
from common import *

METADATA_FILE = "metadata.json"

def load_ip():
    if os.path.exists(METADATA_FILE):
        metadata = ReadMetadata()
        if metadata['server-config']['ip']:
             return metadata['server-config']['ip']
        return find_server()
    return None 

def try_connect(ip, timeout=2):
    try:
        requests.get(f"http://{ip}:5500", timeout=timeout)
        return True
    except:
        return False
    
def find_server(timeout=10):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 9999))
    sock.settimeout(timeout)

    print("Listening for server...")

    try:
        data, addr = sock.recvfrom(1024)
        msg = data.decode()

        if msg.startswith("MONITOR_SERVER"):
            print(f"Server found at: {addr[0]}")
            return addr[0]

    except socket.timeout:
        print("No server found")
        return None


import socket
import time
import threading
from version import __system_name__

HEADER = 64
PORT = 8123
SERVER = "192.168.31.129" 
# SERVER = "192.168.249.236" 
ADDR = (SERVER, PORT)   
FORMATE = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

print(f" Starting client for system: {__system_name__}")
print(f" Connecting to server at {ADDR}")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def socket_client():
    try:
        client.connect(ADDR)
        print(f" Socket client connected to {ADDR}")
    except Exception as e:
        print(f"[ERROR] Socket client failed to connect: {e}")
        return

    def send(msg):
        print(f" Preparing to send message: {msg}")
        message = msg.encode(FORMATE)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMATE)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        print(f" Message sent: {msg}")

    # Register with server
    register_msg = f"REGISTER|{__system_name__}|{PORT}"
    print(f" Sending registration message: {register_msg}")
    send(register_msg)

    while True:
        print("Keeping socket alive...")
        time.sleep(10) 
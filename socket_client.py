import socketio
from common import *
from network import *
from version import __system_id__,__system_name__
import datetime
   
sio = socketio.Client(
    logger=True,
    engineio_logger=True,
    reconnection=True,
    reconnection_attempts=5,
    reconnection_delay=1,
    reconnection_delay_max=5
)

CLIENT_PORT =  5000
SERVER_PORT = 5500

moniterData = MoniterDB()

CONSUMPTION_FILE = "moniter_db.json"

last_modification_file = 0

POLLING_FALLBACK =  'true'  

def get_server_ip():
    cache_ip = load_ip()
    metadata = ReadMetadata()
    
    if cache_ip and try_connect(cache_ip):
        return cache_ip

    print("📡 Discovering server...")
    while True:
        ip = find_server()
        if ip:
            metadata['server-config']['ip'] = ip
            metadata['server-config']['last_connected_at'] = datetime.datetime.now().isoformat()
            WriteMetadata(metadata)
            return ip
        time.sleep(3)
        
SERVER_IP = get_server_ip() 
SERVER_URL = f"http://{SERVER_IP}:{SERVER_PORT}"
print(f"Server IP {SERVER_IP} , Full Address {SERVER_URL}")


def start_socket_client():
    """Improved connection handler with multiple fallback options"""
    transports = ['websocket']
    if POLLING_FALLBACK:
        transports.append('polling')

    while True:
        try:

            print(f"[{SERVER_IP}] Connecting to {SERVER_URL} (transports: {', '.join(transports)})")
            sio.connect(
                SERVER_URL,
                transports=transports,
                headers={
                    'X-Device-Type': 'dispenser',
                    'X-Device-ID': SERVER_IP
                    },
                namespaces=['/'],
                wait_timeout=10
            )
            sio.wait()

        except (socketio.exceptions.ConnectionError, Exception) as e:
            print(f"[{SERVER_IP}] Connection failed: {str(e)}")
            print(f"Retrying in 5 seconds...")
            time.sleep(5)
            
def watch_consumption_file(interval = 2):
        global last_modification_file
        while True:
            try:
                current_mtime = os.path.getmtime(CONSUMPTION_FILE)
                if current_mtime != last_modification_file:
                    last_modification_file = current_mtime
                    print("[INFO] Detected JSON change, emitting data...")
                    data = MoniterDB()
                    metadata = ReadMetadata()
                    sio.emit('consumption_update', {"machine_id":__system_id__,"drink_consumed":data.read(),'machine_logs':metadata})
            except FileNotFoundError:
                print("[WARN] consumption file not found")
            except Exception as e:
                print(f"[ERROR] Watching file: {e}")
            time.sleep(interval)    
            
@sio.event
def connect():
    print(f"[{SERVER_IP}] Connected to dashboard at {SERVER_URL}")
    metadata = ReadMetadata()
    print(moniterData.read())
    sio.emit('register', {
        'machine_id': __system_id__,
        'machine_name': __system_name__,
        'server_url': SERVER_URL,
        'port': CLIENT_PORT,
        'drink_consumed':moniterData.read() ,
        'machine_logs':metadata
    })
    
@sio.event
def disconnect():
    print(f"[{SERVER_IP}] Disconnected from server")

@sio.event
def reconnect():
    print(f"[{SERVER_IP}] Reconnected to server")
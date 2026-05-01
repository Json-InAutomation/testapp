import threading
import time
from socket_client import start_socket_client, watch_consumption_file
from cpu_usage import main as cpu_usage
from RFID_URL import RFID

def main():
    threading.Thread(target=start_socket_client, daemon=True).start()
    threading.Thread(target=watch_consumption_file, daemon=True).start()
    threading.Thread(target=cpu_usage, daemon=True).start()
    threading.Thread(target=RFID, daemon=True).start()

    # threading.Event().wait()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("Worker process interrupted. Exiting...")

if __name__ == "__main__":
    main()

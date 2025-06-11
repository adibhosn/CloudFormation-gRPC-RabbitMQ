import threading
import client

def run_clients():
    for _ in range(100):
        t = threading.Thread(target=client.run)
        t.start()

if __name__ == '__main__':
    run_clients()

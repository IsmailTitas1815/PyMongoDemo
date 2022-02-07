from collector import collector
import time
class DataReceiver:
    def __init__(self):
        pass


if __name__ == "__main__":

    port = int(10003)
    host = "192.168.101.3"

    try:
        recv_obj = collector(host, port)
        st = time.time()
        while recv_obj:
            received_data = recv_obj.receiving_data()
    except KeyboardInterrupt:
        lt = time.time()
        print("\nrun time:",round(lt-st, 2), "seconds")
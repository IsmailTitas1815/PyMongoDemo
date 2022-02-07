import socket

class Receive_from_10003:

    def __init__(self, host, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((host, port))
        while True:
            data = server_socket.recv(1024)
            print("\n"+str(data)+"\n")
            


port = int(10003)
host = "192.168.101.3"

try:
    recv_obj = Receive_from_10003(host, port)
except KeyboardInterrupt:
    print("\nStopped by keyboard\n")

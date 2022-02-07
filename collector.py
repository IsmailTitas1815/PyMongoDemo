import socket
from decoder import Decoder
from pymongo import MongoClient

class collector:
    HOST = None
    PORT = None

    client = MongoClient('localhost', 27017)
    db = client['NewDB']
    col_ModeS_Long = db['ModeS_Long']
    col_ModeS_Short = db['ModeS_Short']
    col_Mode_AC = db['Mode_AC']
    
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect((self.HOST, self.PORT))


    def csv_file_handler(self, col, data):
        try:
            if data:
                col.insert_one(data)
        except Exception as e:
            print("error from csv file handler function", e)


    def get_data(self, data):
        length_of_data = len(data)
        if length_of_data >= 16:
            mode = data[0:2]
            timestamp = data[2:14]
            receiver_level = data[14:16]
            if length_of_data>16:
                msg = data[16:]
            else:
                msg = ""
            if len(msg) in [4,14,28]:
                return {"mode":mode, "timestamp":timestamp, "receiver_level":receiver_level, "msg":msg}
        return


    def store_by_mode(self, data):
        mode = data[:2]
        tuple_data = self.get_data(data)

        if tuple_data:
            if mode == "33":
                self.csv_file_handler(self.col_ModeS_Long, tuple_data)

            elif mode == "32":
                self.csv_file_handler(self.col_ModeS_Short, tuple_data)

            elif mode == "31":
                self.csv_file_handler(self.col_Mode_AC, tuple_data)


    def receiving_data(self):
        data = self.server_socket.recv(1024)
        data_obj = Decoder()
        decoded_data = data_obj.decode_packet_data(data)
        for data in decoded_data:
            self.store_by_mode(data)

        return decoded_data

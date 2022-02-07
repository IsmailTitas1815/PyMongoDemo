import socket
from decoder import Decoder
import csv


class collector:
    HOST = None
    PORT = None
    
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect((self.HOST, self.PORT))


    def csv_file_handler(self, file_name, tuple_data):
        try:
            if file_name and tuple_data:
                file = open('./csv_files/'+file_name, 'a', newline = "\n")
                file_writer = csv.writer(file, delimiter = ",")
                file_writer.writerow(tuple_data)
                file.close()

        except Exception as e:
            print("error from csv file handler function", e)


    def get_tuple_data(self, data):
        length_of_data = len(data)
        if data[:2] =="31":
            print(True, len(data))
        if length_of_data >= 16:
            mode = data[0:2]
            timestamp = data[2:14]
            receiver_level = data[14:16]
            if length_of_data>16:
                msg = data[16:]
            else:
                msg = ""
            if len(msg) in [4,14,28]:
                return (mode, timestamp, receiver_level, msg)
        return


    def store_by_mode(self, data):
        mode = data[:2]
        tuple_data = self.get_tuple_data(data)

        if tuple_data:
            if mode == "33":
                self.csv_file_handler("ModeS_Long.csv", tuple_data)

            elif mode == "32":
                self.csv_file_handler("ModeS_Short.csv", tuple_data)

            elif mode == "31":
                self.csv_file_handler("Mode_AC.csv", tuple_data)


    def receiving_data(self):
        data = self.server_socket.recv(1024)
        data_obj = Decoder()
        decoded_data = data_obj.decode_packet_data(data)
        for data in decoded_data:
            self.store_by_mode(data)

        return decoded_data

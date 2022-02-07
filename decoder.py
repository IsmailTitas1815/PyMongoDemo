class Decoder:
    buffer = ""
    def __init__(self):
        pass

    def decode_packet_data(self, packet_data):
        self.buffer = packet_data
        messages = []
        msg = []
        i = 1
        decoded_data = []
        while i < len(self.buffer):
            if(self.buffer[i: i+2] == [0x1A, 0x1A]):
                msg.append(0x1A)
                i += 1
            elif self.buffer[i] == 0x1A and i == len(self.buffer) - 1:
                msg.append(0x1A)
            elif self.buffer[i] == 0x1A:
                if len(msg) > 0:
                    messages.append(msg)
                    msg = []
            else: 
                msg.append(self.buffer[i])
            i += 1

            if i == len(self.buffer) - 1 and len(msg) > 0:
                messages.append(msg)
        
        for message in messages:
            type = message[0]
            if(type == 0x33):
                temp = "".join('%02x' % i for i in message)
                decoded_data.append(temp)
            elif(type == 0x32):
                temp = "".join('%02x' % i for i in message)
                decoded_data.append(temp)
            elif(type == 0x31):
                temp = "".join('%02x' % i for i in message)
                decoded_data.append(temp)

        return decoded_data
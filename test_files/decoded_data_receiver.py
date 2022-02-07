from decoder import Decoder

# packet_data = b"\x1a3'j\x9d\x8dBL]\x8d\xa3\x86jX\xaf\x96\x8c\xbf\xd6E\xeaCw\x1a2'j\x9d\xe5\x88\x90{\x02\xc5\x88\x13\x0b\xd7\x96\x1a3'j\x9f\x1f.\x15\x1d\x8d\x80\rHX\xd3\x16\x83\xbc\x10d\x0c\x90\x15\x1a3'j\x9fS\x0bmu\x8d\x04\x01CX\xd3\x02\xd7z\x0fY\x95\xd7\x16\x1a3'j\x9fW+\xd2t\x8d\x04\x01C\x99\n\x1c\x01\x80\x04I\xca\xbeG\x1a2'j\x9f\x97\xef;=\x02\xc1\x88\xb1:]\x16\x1a3'j\xa1\x92\xd9\xad\xa0\x8d\x89d\x97\x99\x88\xce\x0e\xb8(\x84Q\x0c-\x1a3'j\xa3\x18\x18\xc5\x1a\x1a\x8d\xa5\xc9\x9eX\xc9\x07Q\x84KQ\xa54\xd2\x1a2'j\xa3:\xb7\xfe:\x02\xc5\x88\xb1\r\x0c\x12\x1a3'j\xa3\xda2\x1a\x1a-\x8dp g\xf8!\x00\x02\x00Ix\xa6\xd4M\x1a3'j\xa4\x85!\xce^\x8dp \xa3\xf8#\x00\x02\x00I\xb8i-q\x1a2'j\xa6\x7fl\xd4\xa9\x02\xa1\x83\xbe\x91G\xb9\x1a2'j\xa6\xa6\xaf\x8d\xab\x02\xa1\x83\xbe\x91G\xb9\x1a2'j\xa7F&>W\x02\xe6\x0f\x1b\x83\xbd\xce\x1a2'j\xa7mu\x99Y\x02\xe6\x0f\x1b\x83\xbd\xce"


class DecodedDataReceiver:
    def __init__(self):
        pass


if __name__ == "__main__":

    # packet_data = b"\x1a3\r\xeavn\xd9\x98\x1e\x8d\x06\xa0RX\xc9\x07\xadd\xd5\x12O\xc0\x91\x1a2\r\xeaz\xa1\xa7P*]s5\xa2\x8e'X\x1a4\r\xea\x80\x00\x00N\x005\x06\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a3\r\xea\x82y\x11\x10%\x80\xe1\x99\x10X\xc9\x07\xad^\xd5\x1dc\xa0\xf5\x1a3\r\xea\x84/^\x82D\x8dp \xa6\xea\x17\x88_\x81\\\x08\x7f\x88R\x1a2\r\xea\x84f\x9f\xc5\x18]\x06\xa0R\x8c5\x1a\x1a\x1a3\r\xea\x84\xc7\xed\x12$\x8dp \xa6XAsR\x0b\xdb\xc5\x0cL\x10\x1a3\r\xea\x85\x03\x12/(\x8ds5\xa2\x90\xb9\x83\xf3\xa9R\x15\x80\x01\xc9"
    packet_data = b'\x1a2\r\xea\xa03P\x06\x1f]\x06\xa0R\x8c5\x1a\x1a\x1a2\r\xea\xa1\x92\x0c\xd7"]\x06\xa1\x9dy\x1dr\x1a3\r\xea\xa3c\xb6\xfc)\x8ds5\xa2\x90\xb9\x83\xf3\xb1R\x06\xcc\xef\x1b\x1a3\r\xea\xa3\xc6\x9c\xccE\x8dp \xa6XAsR\x19\xdb\xbf\xc8n\xfd\x1a3\r\xea\xa6\xee\x8d\xbe.\x8ds5\xa2\x99E\x80\x0b\x88\x04?x\x1a\x1a\xea\x1a2\r\xea\xa8\x8ad\xa7%]p \xa6N\x80-\x1a3\r\xea\xa9^L\x16k\xa0\x00\x12\n\x00\x00\x00\x00\x00\x00\x00\x8a\x8b\x8f'



    data_obj = Decoder()
    decoded_data = data_obj.split_packet_data(packet_data)
    print(*decoded_data, sep="\n")
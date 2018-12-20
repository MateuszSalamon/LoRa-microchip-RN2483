import socket
from sqlite3_my import db_data_method, db_time_method


UDP_IP = "192.168.0.29"

UDP_PORT = 6

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))


while True:

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    # print("received message:",data)

    data2 = str(data)  # data converted to string as to not overshadow important information

    if len(data2) > 150:  # length 150 - to not take date synchronization frames into consideration
        db_data_method(data2)
    elif 30 < len(data2) < 150:
        db_time_method(data2)

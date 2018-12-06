import socket

UDP_IP = "192.168.0.29"

UDP_PORT = 6

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

while True:

    data, addr = sock.recvfrom(512) # buffer size is 512 bytes
    print("received message:",data)
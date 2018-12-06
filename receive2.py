import socket

UDP_IP = "192.168.0.29"

UDP_PORT = 6

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

def data_method(data2):
    tab = ['rxpk', 'tmst', 'chan', 'rfch', 'freq', 'stat', 'modu', 'datr', 'codr', 'lsnr', 'rssi', 'size', 'data']
    tab2 = [None] * len(tab)
    for n in range(0, len(tab)):
        if n == 0:
            tab2[n] = data2[data2.find(tab[n]):len(data2) - 3]
            # print(tab[n] + '= ' + tab2[n])
        elif n < (len(tab) - 1):
            tab2[n] = data2[data2.find(tab[n]) + 6:data2.find(tab[n + 1]) - 2]
            print(tab[n] + '= ' + tab2[n])
        elif n == (len(tab) - 1):
            tab2[n] = data2[data2.find(tab[n]) + 7:len(data2) - 4]
            print(tab[n] + '= ' + tab2[n])
    print(tab2[1:])
    f = open("data_received.txt", "a+")
    for i in range(1, len(tab)):
        f.write(tab[i] + "= " + tab2[i] + '\n')
    f.close()
def time_method(data2):
    tab = ['stat', 'time', 'rxnb', 'rxok', 'rxfw', 'ackr', 'dwnb', 'txnb']
    tab2 = [None] * len(tab)
    for n in range(0, len(tab)):
        if n == 0:
            tab2[n] = data2[data2.find(tab[n]) + 5:len(data2) - 3]
            print(tab[n] + '= ' + tab2[n])
        elif n < (len(tab) - 1):
            tab2[n] = data2[data2.find(tab[n]) + 6:data2.find(tab[n + 1]) - 2]
            print(tab[n] + '= ' + tab2[n])
        elif n == (len(tab) - 1):
            tab2[n] = data2[data2.find(tab[n]) + 6:len(data2) - 2]
            print(tab[n] + '= ' + tab2[n])
    print(tab2[1:])
    f = open("time_received.txt", "a+")
    for i in range(1, len(tab)):
        f.write(tab[i] + "= " + tab2[i] + '\n')
    f.close()


while True:

    data, addr = sock.recvfrom(512) # buffer size is 512 bytes
    # print("received message:",data)

    data2 = str(data)  # data converted to string as to not overshadow important information

    if len(data2) > 150:  # length 150 - to not take date synchronization frames into consideration
        data_method(data2)
    elif 30 < len(data2) < 150:
        time_method(data2)

import socket

UDP_IP = "192.168.0.29"

UDP_PORT = 6

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

while True:

    data, addr = sock.recvfrom(512) # buffer size is 512 bytes
    # print("received message:",data)
    # data = """"', '\x01\xf3k\x00\x124Vx\x87eC!{"rxpk":["tmst":1774837244,"chan":2,"rfch":0,"freq":868.500,"stat":1,"modu":"LORA","datr":"SF12BW125","codr":"4/5","lsnr":7.8,"rssi":-1,"size:25,"data":"QBzcGQAAJwAGIuwRttCmpPgZ2wQ19wcIhw=="}]}')"""
    # data = """', '/x015/xfe/x00/x124Vx/x87eC!["stat":{"time":"2011-01-01T06:29:35Z","rxnb":49,"rxok":25,"rxfw":25,"ackr":0,"dwnb":0,"txnb:0}}')"""
    data2 = str(data)  # data converted to string as to not overshadow important information

    def data_method(data2):
        tab = ['rxpk', 'tmst', 'chan', 'rfch', 'freq', 'stat', 'modu', 'datr', 'codr', 'lsnr', 'rssi', 'size', 'data']
        tab2 = [None] * len(tab)
        for n in range(0, len(tab)):
            if n == 0:
                tab2[n] = data2[data2.find(tab[n]):len(data2) - 3]
                # print(tab[n] + '= ' + tab2[n])
            elif n < (len(tab)-1):
                tab2[n] = data2[data2.find(tab[n]) + 6:data2.find(tab[n + 1]) - 2]
                print(tab[n] + '= ' + tab2[n])
            elif n == (len(tab)-1):
                tab2[n] = data2[data2.find(tab[n]) + 7:len(data2) - 6]
                print(tab[n] + '= ' + tab2[n])

    def time_method(data2):
        tab = ['stat','time','rxnb','rxok','rxfw','ackr','dwnb','txnb']
        tab2 = [None] * len(tab)
        for n in range(0, len(tab)):
            if n == 0:
                tab2[n] = data2[data2.find(tab[n]) + 5:len(data2) - 3]
                print(tab[n] + '= ' + tab2[n])
            elif n < (len(tab)-1):
                tab2[n] = data2[data2.find(tab[n]) + 6:data2.find(tab[n + 1]) - 2]
                print(tab[n] + '= ' + tab2[n])
            elif n == (len(tab)-1):
                tab2[n] = data2[data2.find(tab[n]) + 5:len(data2) - 4]
                print(tab[n] + '= ' + tab2[n])


    if len(data2) > 128:  # length 128 - to not take date synchronization frames into consideration
        data_method(data2)
    if len(data2) > 128:
        time_method(data2)
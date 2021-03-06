
def data_method(data1):
    tab = ['rxpk', 'tmst', 'chan', 'rfch', 'freq', 'stat', 'modu', 'datr', 'codr', 'lsnr', 'rssi', 'size', 'data']
    tab2 = [None] * len(tab)
    for n in range(0, len(tab)):
        if n == 0:
            tab2[n] = data1[data1.find(tab[n]):len(data1) - 3]
            # print(tab[n] + '= ' + tab2[n])
        elif n < (len(tab) - 1):
            tab2[n] = data1[data1.find(tab[n]) + 6:data1.find(tab[n + 1]) - 2]
            # print(tab[n] + '= ' + tab2[n])
        elif n == (len(tab) - 1):
            tab2[n] = data1[data1.find(tab[n]) + 7:len(data1) - 4]
            # print(tab[n] + '= ' + tab2[n])
    # print(tab2[1:])
    # f = open("data_received.txt", "a+")
    # for i in range(1, len(tab)):
    #     f.write(tab[i] + "= " + tab2[i] + '\n')
    # f.close()
    return tab2


def time_method(data1):
    tab3 = ['stat', 'time', 'rxnb', 'rxok', 'rxfw', 'ackr', 'dwnb', 'txnb']
    tab4 = [None] * len(tab3)
    for n in range(0, len(tab3)):
        if n == 0:
            tab4[n] = data1[data1.find(tab3[n]) + 5:len(data1) - 3]
            # print(tab3[n] + '= ' + tab4[n])
        elif n < (len(tab3) - 1):
            tab4[n] = data1[data1.find(tab3[n]) + 6:data1.find(tab3[n + 1]) - 2]
            # print(tab3[n] + '= ' + tab4[n])
        elif n == (len(tab3) - 1):
            tab4[n] = data1[data1.find(tab3[n]) + 6:len(data1) - 2]
            # print(tab3[n] + '= ' + tab4[n])
    # print(tab4[1:])
    # f = open("time_received.txt", "a+")
    # for i in range(1, len(tab3)):
    #     f.write(tab3[i] + "= " + tab4[i] + '\n')
    # f.close()
    return tab4


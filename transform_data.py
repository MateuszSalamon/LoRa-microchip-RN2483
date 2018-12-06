# from receive import data
data = """"', '\x01\xf3k\x00\x124Vx\x87eC!{"rxpk":["tmst":1774837244,"chan":2,"rfch":0,"freq":868.500,"
stat":1,"modu":"LORA","datr":SF12BW125","codr":"4/5","lsnr":7.8,"rssi":-1,"size:25,"data":"QBzcGQAAJwAGIuwRttCmpPgZ2wQ19wcIhw=="}]}')"""

data2 = str(data)


def ignore():
    print('keep alive interval')

def table_method(data2):
    tab = ['rxpk','tmst','chan','rfch','freq','stat','modu','datr','codr','lsnr','rssi','size','data']
    tab2 = ['1','2','3','4','5','6','7','8','9','0','1','2','2','3','4','5','6']
    for n in range (0,len(tab)):
        if n == 0:
            tab2[n] = data2[data2.find(tab[n]):len(data2)-3]
            print(tab[n] +'= ' + tab2[n])
        elif n < 12:
            tab2[n] = data2[data2.find(tab[n])+6:data2.find(tab[n+1])-2]
            print(tab[n] + '= ' + tab2[n])
        elif n == 12:
            tab2[n] = data2[data2.find(tab[n])+7:len(data2)-6]
            print(tab[n] + '= ' + tab2[n])


if len(data2) > 27:
    table_method(data2)





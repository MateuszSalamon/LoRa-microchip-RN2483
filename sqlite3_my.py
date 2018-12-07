# Using sqlite transforms data received from ethernet port in receive2.py
# into an SQL table

import sqlite3
from transform_data import data_method, time_method


# rxpk is equal to all data sent by the ethernet port and is disabled to save space
# to enable rxpk modify c.execute from "rxpk" to tab5[0]


def db_data_method(data1):
    conn = sqlite3.connect("LoRa_db.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS lora (
                rxpk text, tmst text, chan text, rfch text,
                freq text, stat text, modu text, datr text,
                codr text, lsnr text, rssi text, size text,
                data text
                )""")

    tab5 = data_method(data1)
    c.execute("""INSERT INTO lora VALUES
     (?,?,?,?,?,?,?,?,?,?,?,?,?)
     """, ("rxpk",tab5[1],tab5[2],tab5[3],tab5[4],tab5[5],tab5[6],tab5[7],tab5[8],tab5[9],
           tab5[10],tab5[11],tab5[12]))

    c.execute("SELECT * FROM lora WHERE chan ='2'")
    print(c.fetchall())
    conn.commit()
    conn.close()


def db_time_method(data1):
    conn = sqlite3.connect("LoRa_db.db")
    c = conn.cursor()


    c.execute("""CREATE TABLE IF NOT EXISTS time (
                stat text, time text, rxnb text, rxok text,
                rxfw text, ackr text, dwnb text, txnb text
                )""")

    tab5 = time_method(data1)
    c.execute("""INSERT INTO lora VALUES
         (?,?,?,?,?,?,?,?)
         """, ("stat", tab5[1], tab5[2], tab5[3], tab5[4], tab5[5], tab5[6], tab5[7]))

    c.execute("SELECT * FROM lora WHERE txnb ='0'")
    print(c.fetchall())
    conn.commit()
    conn.close()






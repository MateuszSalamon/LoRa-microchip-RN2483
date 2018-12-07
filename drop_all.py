import sqlite3
print("Enter password: ")
password = str(input())

if password == "1234":
    print("password accepted cleaning the database now")
    conn = sqlite3.connect("LoRa_db.db")
    c = conn.cursor()

    c.execute("""DROP TABLE lora;""") # data remove table

    c.execute("""DROP TABLE time;""") # time remove table

    conn.commit()
    conn.close()
else:
    print("wrong password")
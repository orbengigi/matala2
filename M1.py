import os.path
import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

c.execute("""drop table if exists nmea""")

conn.commit()

c.execute("""create table nmea (
    ID INT PRIMARY KEY     NOT NULL,
    TIME              TEXT    NOT NULL,
    LATITUDE           TEXT    NOT NULL,
    NORTH           TEXT    NOT NULL,
    LONGTITUDE           TEXT    NOT NULL,
    EAST           TEXT    NOT NULL,
    QUALITY           TEXT    NOT NULL,
    NOS           TEXT    NOT NULL,
    HDOP           TEXT    NOT NULL,
    ATITUDE             TEXT    NOT NULL,
    HOG               TEXT    NOT NULL)""")

conn.close()

"""def read_dir(str):
    if os.path.isdir(str):
        for file in os.listdir(str):
            if ".nmea" in file:
                read_file(file)
                """


def read_file(str):
    with open (str,'r')as f:
        for x in f:
            if "GPGGA" not in x:
                continue

            create_DB(x)

def create_DB(str):
    list=str.split(",")
    # Insert a row of data
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
  #  c.execute("insert into nmea values (1,?,?,?,?,?,?,?,?,?,? )"([list[1]],[list[2]],[list[3]],[list[4]],[list[5]],[list[6]],
   #           [list[7]],[[list[8]],[list[9]],[list[10]]))
    c.execute("insert into nmea values (1,'2','3','4','5','6','7','8','9','10','11' )")
    c.execute("insert into nmea values (2,'2','3','4','5','6','7','8','9','10','11' )")
    c.execute("insert into nmea values (3,'2','3','4','5','6','7','8','9','10','11' )")
    c.execute("insert into nmea values (4,'2','3','4','5','6','7','8','9','10','11' )")
    c.execute("insert into nmea values (5,'2','3','4','5','6','7','8','9','10','11' )")
    conn.commit()
    conn.close()



read_file("c:\\nmea\\nmea\\A.nmea")
conn = sqlite3.connect('test.db')
c = conn.cursor()

for row in c:
    print(row)

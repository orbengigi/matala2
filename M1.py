import os.path
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
c.execute('drop table if exists nmea')
c.execute('''CREATE TABLE nmea
    (time text, latitude text,north text, longtitude text,
    east text,quality text, nos text, hdop text, altitude text,
    hog text)''')

def read_dir(str):
    if os.path.isdir(str):
       for file in os.listdir(str):
           if ".nmea" in file:
               read_file(file)


def read_file(str):
    with open (str,'r')as f:
        for x in f:
            create_DB(x)

def create_DB(str):
    list1=str.split(",")
    print(list1)
    # Insert a row of data
    c.execute("INSERT INTO nmea VALUES (?,?,?,?,?,?,?,?,?,?)",([list1[1]], [list1[2]], [list1[3]], [list1[4]],[list1[5]], [list1[6]],[list1[7]], [list1[8]], [list1[9]], [list1[10]]))
    conn.commit()



read_file("2016-03-30 10_13_22.nmea")
conn.close()
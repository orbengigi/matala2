import os.path
import sqlite3

i=0
conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table

def read_dir(str):
    if os.path.isdir(str):
       for file in os.listdir(str):
           if ".nmea" in file:
               i = i + 1
               read_file(file)


def read_file(str1):
    with open (str1,'r')as f:
        c.execute('drop table if exists nmea' + str(i))
        c.execute('''CREATE TABLE nmea''' + str(i) + '''
                (time text, latitude text,north text, longtitude text,
                east text,quality text, nos text, hdop text, altitude text,
                hog text)''')
        for x in f:
            if "GPGGA" in x:
                create_DB(x)

def create_DB(str1):
    list1=str1.split(",")
    # Insert a row of data
    c.execute("INSERT INTO nmea"+str(i)+" VALUES (?,?,?,?,?,?,?,?,?,?)",(list1[1], list1[2], list1[3], list1[4],list1[5], list1[6],list1[7], list1[8], list1[9], list1[10]))
    conn.commit()



read_file("2016-03-30 10_13_22.nmea")
conn.close()
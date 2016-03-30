import os.path
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE cde
    (ID INT PRIMARY KEY     NOT NULL, time text, latitude text,north text, longtitude text,east text,
    quality text, nos text, hdop text, altitude text, hog text)''')

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
    list=str.split(",")
    print (type(list[1]))
    # Insert a row of data
    c.execute("INSERT INTO cde VALUES (1, list[1], list[2], list[3], list[4],"
              " list[5], list[6], list[7], list[8], list[9], list[10])")
    conn.commit()






# Save (commit) the changes


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

read_dir("c:\\")
conn.close()
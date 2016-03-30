import os.path
import sqlite3


conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
total=0

def read_dir(str):
    i=0
    global total
    if os.path.isdir(str):
       for file in os.listdir(str):
           if ".nmea" in file:
               i=i+1
               read_file(str+"\\"+file,i)
               total = i

def read_file(str1,i):
    with open (str1,'r')as f:
        c.execute('drop table if exists nmea' + str(i))
        c.execute('''CREATE TABLE nmea''' + str(i) + '''
                (time text, latitude text,north text, longtitude text,
                east text,quality text, nos text, hdop text, altitude text,
                hog text)''')
        for x in f:
            if "GPGGA" in x:
                create_DB(x,i)

def create_DB(str1,i):
    list1=str1.split(",")
    # Insert a row of data
    c.execute("INSERT INTO nmea"+str(i)+" VALUES (?,?,?,?,?,?,?,?,?,?)",(list1[1], list1[2], list1[3], list1[4],list1[5], list1[6],list1[7], list1[8], list1[9], list1[10]))
    conn.commit()


read_dir("C:\\Users\\or\\PycharmProjects\\matala2\\nmea")
#read_file("2016-03-30 10_13_22.nmea")
print('total= '+str(total))
conn.close()
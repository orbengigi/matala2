import os.path
import sqlite3



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
    return i

def read_file(str1,i):
    with open (str1,'r')as f:
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('drop table if exists nmea' + str(i))
        c.execute('''CREATE TABLE nmea''' + str(i) + '''
                (time text, latitude text,north text, longtitude text,
                east text,quality text, nos text, hdop text, altitude text,
                hog text,speed text,date text)''')
        list=f.readlines()
        for x in range(0, len(list)-1,2):
                load_DB(list[x],list[x+1],i)
        conn.close()
    return 1

def load_DB(str1,str2,i):
    list1=str1.split(",")
    list2=str2.split(",")
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Insert a row of data
    c.execute("INSERT INTO nmea"+str(i)+" VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(list1[1], list1[2], list1[3], list1[4],list1[5], list1[6],list1[7], list1[8], list1[9], list1[10],list2[7],list2[9]))
    conn.commit()
    conn.close()


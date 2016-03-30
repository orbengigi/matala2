import M1 as m
import nmea_to_csv as c

i=m.read_dir("C:\\nmea\\nmea")
print (i)
for x in range (1,i+1):
    c.create_csv(x)


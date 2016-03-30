import M1 as m
import nmea_to_csv as c

i=m.read_dir("C:\\Users\\or\\PycharmProjects\\matala2\\nmea")
print (i)
for x in range (i):
    c.create_csv(x)

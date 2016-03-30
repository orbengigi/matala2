
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os.path
import sqlite3
import time

my_category = 0

database =sqlite3.connect('example.db')
pois = database.execute("SELECT * FROM nmea" + str(1))


file = 'file'+str(1)+'.kml'
FILE = open(file,'w')
FILE.truncate(0)

FILE.write('<?xml version="1.0" encoding="iso-8859-1"?>\n')
FILE.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
FILE.write('<Document>\n')
FILE.write('<Folder>\n')

FILE.write('<name>Point Features</name>\n')
FILE.write('<description>Point Features</description>\n')

i = 1
for poi in pois:
	print('%s : %s, %s' % (poi, poi[2], poi[1],))
	FILE.write('<Placemark>\n')
	FILE.write('<name><![CDATA[%i]]></name>\n' % i)
	FILE.write('<description><![CDATA[Lat: %s <br> Lon: %s<br>]]></description>\n' % (poi[1],poi[2]) )
	FILE.write('<Point>\n')
	lat = float(poi[1][:2]) + (float(poi[1][2:]) / 60)
	lon = float(poi[3][:3]) + (float(poi[3][3:]) / 60)
	FILE.write('<coordinates>%s,%s,%s</coordinates>\n' % (str(lon),str(lat),poi[8]))
	FILE.write('</Point>\n')
	FILE.write('</Placemark>\n')
	i = i + 1

FILE.write('</Folder>\n')
FILE.write('</Document>\n')
FILE.write('</kml>\n')
FILE.close()
database.close()


#	db_call = "INSERT INTO poi (idmd5, lat, lon, visibility, cat, subcat, keywords, desc, price_range, extended_open) VALUES (?,?,?,?,?,?,?,?,?,?) "
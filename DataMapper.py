import sqlite3
import json
import codecs
import os
import pathlib
print('''Meteorite Data Explorer Copyright (C) 2018 DigiBrkr This program comes with ABSOLUTELY NO WARRANTY; \n \nThis is free software, and you are welcome to redistribute it under certain conditions. \n
See LICENSE.md for details. \n''')

print('Processing data please wait momentarily. ')
#get the data
dbConnection = sqlite3.connect('index.sqlite')
dbCursor = dbConnection.cursor()
dbCursor.execute ('SELECT DISTINCT Geolocation FROM Geolocations WHERE Geolocation != "none"')
geolocations = dbCursor.fetchall()

#check for and remove existing data
locations = pathlib.Path('locations.js')
if locations.exists():
    os.remove('locations.js')
#crate the new file
locations = codecs.open('locations.js', 'w', "utf-8" )
locations.write("Data = [\n")
#put the data in the file
count = 0
for location in geolocations:
    location = str(location)
    location = location.split(",")
    latitude = location[1].strip("'")
    longitude = location[0].strip("(")
    longitude = longitude.strip("'")
    try:
        locations.write("["+latitude+","+longitude+","+"]"+","+"\n ")
        count = count + 1
    except:
        continue

locations.write("];\n")
locations.close()
dbCursor.close()
print(count, "Locations sucesfully written to disk.\n")
print("Please open locations.html in your web browser to view the data.")

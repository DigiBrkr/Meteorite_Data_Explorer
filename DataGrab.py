#This file is used to pull all the data from the NASA server into the file named raw.sqlite
import sqlite3
import ssl
import sys
import json
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
print('''Meteorite Data Explorer Copyright (C) 2018 DigiBrkr This program comes with ABSOLUTELY NO WARRANTY; \n \nThis is free software, and you are welcome to redistribute it under certain conditions. \n
See LICENSE.md for details. \n''')

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Make the database
db = sqlite3.connect('raw.sqlite')
dbCursor = db.cursor()
#Wipe out any existing databse

dbCursor.execute('''DROP TABLE IF EXISTS Meteorites ;''')

#Make the new table
dbCursor.execute('''CREATE TABLE Meteorites(name TEXT, id INT, nametype TEXT, recclass TEXT,
mass INT, fall TEXT, year TEXT, reclat TEXT, reclong TEXT, geolocation TEXT) ''')

#Grab the data from NASA
#we use 20000000 ad the limit because that *should* give us all the data the is.
url = "https://data.nasa.gov/resource/y77d-th95.json?%24limit=20000000"

try:
    print("Downloading data. This may take some time depending on your Internet connection. ")
    data = urllib.request.urlopen(url, context=ctx)

except:
    print("******** ERROR could not retrive data please check the output below ********")
    print("ERROR:", data.getcode(), url)

#Decode the data into something python can understand

data = data.read().decode()

print("Data is", sys.getsizeof(data),"bytes long")

#Put the retrived data into json format

try:
    data = json.loads(data)
except:
    print("******** ERROR json could not parse the data. Check the data below and try again. ********")
    print(data)


#Put the data into the database
count = -1
maxCount = len(data)
print("Data sanitisation in progress please wait")
for meteorite in data:
    count = count + 1
# for loops to clean up the data
    name = meteorite.get("name")
    try:
        name = str(name)
    except:
        name = "no name available"
    mID = meteorite.get("id")
    try:
        mID = int(mID)
    except:
            mID = 0

    nametype = meteorite.get("nametype")
    try:
        nametype = str(nametype)
    except:
        nametype = "nametype not available"

    recclass = meteorite.get("recclass")
    try:
        recclass = str(recclass)
    except:
        recclass = "recclass not available"

    mass = meteorite.get("mass")
    try:
        mass = int(mass)
    except:
        mass = 0
    fall = meteorite.get("fall")
    try:
        fall = str(fall)
    except:
        fall = "unknown"

    year = meteorite.get("year")
    try:
        year = str(year)
    except:
        year = "none"


    name = meteorite.get("name")
    try:
        name = str(name)
    except:
        name = "no name available"

    mID = meteorite.get("id")
    try:
        mID = int(mID)
    except:
            mID = 0

    nametype = meteorite.get("nametype")
    try:
        nametype = str(nametype)
    except:
        nametype = "nametype not available"

    recclass = meteorite.get("recclass")
    try:
        recclass = str(recclass)
    except:
        recclass = "recclass not available"

    mass = meteorite.get("mass")
    try:
        mass = int(mass)
    except:
        mass = 0
    fall = meteorite.get("fall")
    try:
        fall = str(fall)
    except:
        fall = "unknown"

    year = meteorite.get("year")
    try:
        year = str(year)
    except:
        year = "none"

    reclat = meteorite.get("reclat")
    try:
        reclat = float(reclat)
    except:
        reclat = 0

    reclong = meteorite.get("reclong")
    try:
        reclong = float(reclong)
    except:
        reclong = 0

    geolocation = meteorite.get("geolocation")

    try:
        geolocation = str(geolocation)
    except:
            geolocation = "none"

        #place the data into th db
    dbCursor.execute('''INSERT OR IGNORE INTO Meteorites (name, id, nametype, recclass, mass, fall, year, reclat, reclong, geolocation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (name, mID, nametype, recclass, mass, fall, year, reclat, reclong, geolocation))

#write to disk
db.commit()
dbCursor.close()
print("Data successfully written to disk")

import sqlite3
print('''Meteorite Data Explorer Copyright (C) 2018 DigiBrkr This program comes with ABSOLUTELY NO WARRANTY; \n \nThis is free software, and you are welcome to redistribute it under certain conditions. \n
See LICENSE.md for details. \n''')
loopCount = 0

#connect to raw.sqlite
rawConnection = sqlite3.connect('raw.sqlite')
rawCursor = rawConnection.cursor()
#make the new and faster database
indexDB = sqlite3.connect('index.sqlite')
indexCursor = indexDB.cursor()

#get rid of anhy exsiting tables
indexCursor.execute('DROP TABLE IF EXISTS Names')
indexCursor.execute('DROP TABLE IF EXISTS mID')
indexCursor.execute('DROP TABLE IF EXISTS Nametypes')
indexCursor.execute('DROP TABLE IF EXISTS Recclasses')
indexCursor.execute('DROP TABLE IF EXISTS Masses')
indexCursor.execute('DROP TABLE IF EXISTS Falls')
indexCursor.execute('DROP TABLE IF EXISTS Years')
indexCursor.execute('DROP TABLE IF EXISTS Reclats')
indexCursor.execute('DROP TABLE IF EXISTS Reclongs')
indexCursor.execute('DROP TABLE IF EXISTS Geolocations')

#make the new tables
indexCursor.execute('''CREATE TABLE IF NOT EXISTS Names
(uID INTEGER PRIMARY KEY, Name TEXT )''')

indexCursor.execute('''CREATE TABLE IF NOT EXISTS mIDs
(uID INTEGER PRIMARY KEY, mID INTEGER )''')

indexCursor.execute('''CREATE TABLE IF NOT EXISTS Nametypes
(uID INTEGER PRIMARY KEY, nametype TEXT )''')

indexCursor.execute('''CREATE TABLE IF NOT EXISTS Recclasses
(uID INTEGER PRIMARY KEY, Recclass TEXT )''')

indexCursor.execute('''CREATE TABLE IF NOT EXISTS Masses
(uID INTEGER PRIMARY KEY, Mass INT)''')

indexCursor.execute('''CREATE TABLE IF NOT EXISTS Falls
(uID INTEGER PRIMARY KEY, Fall TEXT) ''')

indexCursor.execute('''CREATE TABLE IF NOT EXISTS Years
(uID INTEGER PRIMARY KEY, year INTEGER) ''')

indexCursor.execute('''CREATE TABLE IF NOT EXISTS Reclats
(uID INTEGER PRIMARY KEY, Reclat REAL) ''')

indexCursor.execute('''CREATE TABLE IF NOT EXISTS Reclongs
(uID INTEGER PRIMARY KEY, Reclong REAL) ''')

indexCursor.execute('''CREATE TABLE IF NOT EXISTS Geolocations
(uID INTEGER PRIMARY KEY, Geolocation TEXT) ''')


#deal with names
rawCursor.execute('SELECT name FROM Meteorites')
names = rawCursor.fetchall()
print("Sanitizing Data. This may take a while depending on the speed of your computer. \n")

for name in names:
    name = str(name)
    #this code is hideous but it's the least ugly option to my knowledge
    name = name.strip("(")
    name = name.strip(")")
    name = name.strip("'")
    name = name.strip(",")
    name = name.strip("'")
    name = name.strip()
    name = name.strip("'")

    loopCount = loopCount + 1

    indexCursor.execute('INSERT OR IGNORE INTO Names(Name) VALUES (?)', (name,))
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

#deal with mIDs

rawCursor.execute('SELECT id FROM Meteorites')
mIDs = rawCursor.fetchall()

for mID in mIDs:
    #need to convert to a string to clean it up before we can go to an int
    mID = str(mID)
    mID = mID.strip("(")
    mID = mID.strip(")")
    mID = mID.strip(",")

    #now we can convert to an int
    mID = int(mID)
    indexCursor.execute('INSERT OR IGNORE INTO mIDs(mID) VALUES (?)', (mID,))
    loopCount = loopCount + 1
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

#deal with Nametypes

rawCursor.execute('SELECT nametype FROM Meteorites')
nametypes = rawCursor.fetchall()
for nametype in nametypes:
    #convert to string
    nametype = str(nametype)
    #de-junk
    nametype = nametype.strip("(")
    nametype = nametype.strip(")")
    nametype = nametype.strip("'")
    nametype = nametype.strip(",")
    nametype = nametype.strip("'")
    nametype = nametype.strip("'")
    nametype = nametype.strip()
    nametype = nametype.strip("'")
    indexCursor.execute('INSERT OR IGNORE INTO Nametypes(nametype) VALUES (?)', (nametype,))
    loopCount = loopCount + 1
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

#deal with recclass

rawCursor.execute('SELECT recclass FROM Meteorites')
recclasses = rawCursor.fetchall()

for recclass in recclasses:
    #convert to string
    recclass = str(recclass)
    #de-junk
    recclass = recclass.strip("(")
    recclass = recclass.strip(")")
    recclass = recclass.strip("'")
    recclass = recclass.strip("'")
    recclass = recclass.strip(",")
    recclass = recclass.strip("'")
    recclass = recclass.strip()
    recclass = recclass[1:]
    recclass = recclass.strip("'")
    indexCursor.execute('INSERT OR IGNORE INTO Recclasses(recclass) VALUES (?)', (recclass,))
    loopCount = loopCount + 1
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

#deal with mass

rawCursor.execute('SELECT mass FROM Meteorites')
masses = rawCursor.fetchall()
for mass in masses:
    #we must convert to string and clean before we can go to an int
    mass = str(mass)
    mass = mass.strip("(")
    mass = mass.strip(")")
    mass = mass.strip("'")
    mass = mass.strip("'")
    mass = mass.strip(",")
    mass = int(mass)
    indexCursor.execute('INSERT OR IGNORE INTO Masses(mass) VALUES (?)', (mass,))
    loopCount = loopCount + 1
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

#deal with fall
rawCursor.execute('SELECT fall FROM Meteorites')
falls = rawCursor.fetchall()
for fall in falls:

    #convert to string
    fall = str(fall)
    #de-junk
    fall = fall.strip("(")
    fall = fall.strip(")")
    fall = fall.strip("'")
    fall = fall.strip("'")
    fall = fall.strip(",")
    fall = fall.strip("'")
    fall = fall.strip("'")
    fall = fall.strip()
    fall = fall.strip("'")
    indexCursor.execute('INSERT OR IGNORE INTO Falls(Fall) VALUES (?)', (fall,))
    loopCount = loopCount + 1
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

#deal with year
rawCursor.execute('SELECT year FROM Meteorites')
years = rawCursor.fetchall()
for year in years:
    #convert to string
    year = str(year)
    #de=junk
    year = year.strip("(")
    year = year.strip(")")
    year = year.strip("'")
    year = year.strip("'")
    year = year.strip(",")
    year = year.strip("'")
    year = year.strip()
    year = year.strip("'")
    #year is in the floating timestamp format but it just has the year so we can throw away the rest
    year = year.split("-")
    year = year[0]
    try:
        #convert to int but be prepared for bad data
        year = int(year)
    except:
        year = 0
    indexCursor.execute('INSERT OR IGNORE INTO Years(year) VALUES (?)', (year,))
    loopCount = loopCount + 1
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

#deal with Reclats
rawCursor.execute('SELECT reclat FROM Meteorites')
reclats = rawCursor.fetchall()
for reclat in reclats:
    #convert to string
    reclat = str(reclat)
    #de-junk
    reclat = reclat.strip("(")
    reclat = reclat.strip(")")
    reclat = reclat.strip("'")
    reclat = reclat.strip("'")
    reclat = reclat.strip(",")
    reclat = reclat.strip("'")
    reclat = reclat.strip("u")
    reclat = reclat.strip("'")
    try:
        #conver to float
        reclat = float(reclat)
    except:
        reclat = 0
    indexCursor.execute('INSERT OR IGNORE INTO Reclats(reclat) VALUES (?)', (reclat,))
    loopCount = loopCount + 1
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

#deal with reclongs
rawCursor.execute('SELECT reclong FROM Meteorites')
reclongs = rawCursor.fetchall()
for reclong in reclongs:
    #convert to string
    reclong = str(reclong)
    #de-junk
    reclong = reclong.strip("(")
    reclong = reclong.strip(")")
    reclong = reclong.strip("'")
    reclong = reclong.strip("'")
    reclong = reclong.strip(",")
    reclong = reclong.strip("'")
    reclong = reclong.strip("u")
    reclong = reclong.strip("'")
    try:
        #Conver to float
        reclong = float(reclong)
    except:
        reclong = 0
    indexCursor.execute('INSERT OR IGNORE INTO Reclongs(reclong) VALUES (?)', (reclong,))
    loopCount = loopCount + 1
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

#deal with geolocations
rawCursor.execute('SELECT geolocation FROM Meteorites')
geolocations = rawCursor.fetchall()

for geolocation in geolocations:
    #convert to string
    geolocation = str(geolocation)
    geolocation = geolocation.split(":")
    try:
        geolocation = geolocation[1]
    except:
        geolocation = "none"


    geolocation = geolocation[:-9]
    geolocation = geolocation.strip()
    geolocation = geolocation.strip("[")

    #set all bad data to "none"
    if len(geolocation) <= 0:
        geolocation = "none"

    if geolocation == "0, 0":
        geolocation = "none"

    indexCursor.execute('INSERT OR IGNORE INTO Geolocations(geolocation) VALUES (?)', (geolocation,))

    loopCount = loopCount + 1
    if loopCount == 10:
        indexDB.commit()
        loopCount = 0
        continue
    else:
        continue
else:
    loopCount = 0

indexDB.commit()
indexDB.close()
print("Data sanitisation complete. This Program will now exit.")

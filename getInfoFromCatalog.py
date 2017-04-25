#!/bin/env python
''' This script contains examples of how to get information out of a
    catalog built by the fdsn iris client
'''
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.core.event import Origin
import returnDistDeg
from getEvents4Station import getEvents4Station 

client = Client("IRIS")

net = "IU"
sta = "ANMO"
staLat = 34.945910
staLon = -106.457200
staDepth = -1820

startTime = UTCDateTime("2016-01-01T00:00:00")
endTime = UTCDateTime.now() # use current time
minRad=25
maxRad=90
minMag=6.0

EventCatalog = getEvents4Station(staLat,staLon,startTime,endTime,minRad,maxRad,minMag)

print(EventCatalog)
for event in EventCatalog:
    print(event.origins[0]['time'])
    time = event.origins[0]['time']
    doy=time.julday
    evLat=event.origins[0]['latitude']
    evLon=event.origins[0]['longitude']
    print ('Event lat, lon: '+str(evLat)+', '+str(evLon))
    print doy

    

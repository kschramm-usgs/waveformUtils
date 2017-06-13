#!/bin/env python

from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.geodetics import locations2degrees
from getPwaveArrival import getPwaveArrival
import numpy as np


f = open("Output.txt", 'w')
client = Client("IRIS")
startTime = UTCDateTime("2016-01-01T00:00:00")
endTime = UTCDateTime("2017-05-26T00:00:00")
minMag = 7.0
EventCatalog = client.get_events(starttime=startTime,endtime=endTime,\
        minmagnitude=minMag)
staLat = 34.945910
staLon = -106.457200
#EventCatalog
EventCatalog.count()
for event in EventCatalog:
    print(event.origins)
    evLat=event.origins[0]['latitude']
    evLon=event.origins[0]['longitude']
    evDepth=event.origins[0]['depth']/1000.0
    evYear=event.time[0]
    print(evYear)
    
#    DegDist = locations2degrees(staLat,staLon,evLat,evLon)
#    pTime = getPwaveArrival(evDepth,DegDist)
#    dataStart = event.origins[0]['time']+pTime-10
#    dataEnd = event.origins[0]['time']+pTime+60
#    string = str(evLat)+ "   "+str(evLon) + "   "+str(evDepth)+"\n"
    f.write("%10.4f %10.4f %10.2f\n" % (evLat,evLon,evDepth))

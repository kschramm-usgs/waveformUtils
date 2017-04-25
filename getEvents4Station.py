#!/bin/env python

from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.core.event import Origin
import returnDistDeg

stLat = 34.945910
stLon = -106.457200
stDepth = -1820

net = "IU"
sta = ["ANMO"]
chan = "00"
comp = "BH*"
debug="True"

client = Client("IRIS")

startTime = UTCDateTime("2016-01-01T00:00:00")
endTime = UTCDateTime("2017-04-24T00:00:00")

EventCatalog = client.get_events(starttime=startTime,endtime=endTime,\
                                 latitude=stLat,longitude=stLon, \
                                 minradius=25, maxradius=90, \
                                 minmagnitude=6.0)

print(EventCatalog)
for event in EventCatalog:
    print(event.origins[0]['time'])
    print(event.times)
    #print(event.origins.time)
    #print(origins.time)
    #print(event[1])


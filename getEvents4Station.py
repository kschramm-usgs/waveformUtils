#!/bin/env python
def getEvents4Station(stLat,stLon,startTime,endTime,minRad,maxRad,minMag):
    ''' This will collect a set of events for a station.
        input: station latitude, station longitude, 
               starting and ending times(UTC date time),
               minimum and maximum degrees distance from station, 
               minimum magnitude
        output: a catalog of events
    '''
    from obspy import UTCDateTime
    from obspy.clients.fdsn import Client

    #stLat = 34.945910
    #stLon = -106.457200
    #startTime = UTCDateTime("2016-01-01T00:00:00")
    #endTime = UTCDateTime("2017-04-24T00:00:00")

    client = Client("IRIS")
    EventCatalog = client.get_events(starttime=startTime,endtime=endTime,\
                                 latitude=stLat,longitude=stLon, \
                                 minradius=minRad, maxradius=maxRad, \
                                 minmagnitude=minMag)
    return EventCatalog

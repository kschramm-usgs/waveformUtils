#!/bin/env python

from obspy.clients.fdsn import Client
from obspy import UTCDateTime

client = Client("IRIS")

starttime = UTCDateTime("2016-11-01")
endtime = UTCDateTime("2017-03-07")

cat = client.get_events(starttime=starttime, endtime=endtime,
                        minmagnitude=5, minlatitude=40, maxlatitude=60,
                        minlongitude=0, maxlongitude=40)
print(cat)
#print(CatalogObject.__str__(print_all=True))

cat.plot()

#!/bin/env python

#def getdata(net, sta, eventtime, lents, debug=False):
#    """
#        This function goes to both archives and gets the data.
#        At ASL the archives are located in:
#            /tr1/telemetry_days
#          or
#           /msd
#        depending on how long since the event passed.
#
#        this gets info for only one station.  
#
#        from Adam Ringler
#    """

from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy.taup import TauPyModel
from obspy.core import *
import glob

# event time - this can be calculate based on the p-wave arrival
# this is for an event in Bolivia

eventTime = UTCDateTime("2017-02-21T14:09:04.000")
pWaveArrTime = 652
stime = eventTime+pWaveArrTime
etime = stime+60

stLat = 34.945910
stLon = -106.457200
stDepth = -1820

EventCatalog = getEvents4Station(staLat,staLon,startTime,endTime,minRad,maxRad,minMag)

# Current default is LH add BH later

#if (net in set(['GT'])) or (sta == 'KBL'):
#    chan = 'BH'

#changing this to be off of msd - don't want to deal w/ tr1 paths
# Grab the data locations
datalocs = ['/msd/']

files = []
# Grab the files and deal with edge cases
for dataloc in datalocs:
    for year in range(stime.year, etime.year+1):
        for day in range(stime.julday, etime.julday+1):
            string = dataloc + net + '_' + sta + '/' + \
                    str(year) + '/*' + str(day).zfill(3)+\
                    '/*'+ chan + '*'+comp+'*.seed'

            print(string)
            files += glob.glob(string)
            print(string+ '/*'+ chan + '*'+comp+'*.seed')
            print(files)
            

# needed: from obspy.core import * for the following line to work
st = Stream()
for curfile in files:
    try:
        print('trying to read in file: '+ curfile)
        st += read(curfile, starttime=stime, endtime=etime)
    except:
        if debug:
            print 'Unable to get data ' + curfile
##st.merge(fill_value='latest')
st.plot()
if debug:
        print 'We have data'
#return st



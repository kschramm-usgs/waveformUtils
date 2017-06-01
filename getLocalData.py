#!/bin/env python

#def getdata(net, staLat, staLon,beginTime,endTime,):
# we should take some of this stuff out because we are doing too
# many things in one piece of code
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
from obspy.geodetics.base import locations2degrees
import glob
from getEvents4Station import getEvents4Station
from getPwaveArrival import getPwaveArrival
from numpy import array
from getMSDdata import getMSDdata
from getTR1data import getTR1data

# event time - this can be calculate based on the p-wave arrival
# this is for an event in Bolivia

#eventTime = UTCDateTime("2017-02-21T14:09:04.000")
#pWaveArrTime = 652
#stime = eventTime+pWaveArrTime
#etime = stime+60
#set time to search for events.
begintime=UTCDateTime("2017-05-27")
endtime=UTCDateTime.now()

net = "IU"
sta= "ANMO"
staLat = 34.945910
staLon = -106.457200
staDepth = -1820
chan = "00"
comp = "BH*"

minRad=25
maxRad=90
minMag=6.0


EventCatalog = getEvents4Station(staLat,staLon,begintime,endtime,minRad,maxRad,minMag)
print("There are "+ str(EventCatalog.count()) + " events in the catalog")

#need to get data based on event arrival time
# step 1. calculate station/event distance
# step 2. calc phase arrival time
#dataStart=[]
#dataEnd=[]
for event in EventCatalog:
    evLat=event.origins[0]['latitude']
    evLon=event.origins[0]['longitude']
    evDepth=event.origins[0]['depth']/1000.0
    DegDist = locations2degrees(staLat,staLon,evLat,evLon)
    pTime = getPwaveArrival(evDepth,DegDist)
    dataStart = event.origins[0]['time']+pTime-10
    dataEnd = event.origins[0]['time']+pTime+60
    print(dataStart.year)
    
    #dataStream=getMSDdata(sta,net,chan,comp,dataStart,dataEnd)
    dataStream=getTR1data(sta,net,chan,comp,dataStart,dataEnd)
    dataStream.plot()

    
##count =0
#for date in dataStart:
#    print(date.year)
#    count =count+1
##put in check for day
##if stime.julday != etime.julday:
##    print('End time on different day, need to merge seismograms.')
#
##changing this to be off of msd - don't want to deal w/ tr1 paths
## Grab the data locations
#dataloc = '/msd/'
#
## this is not looping over the events... need to get it plotting a
## wavefore for each event.
#for stime in dataStart:
#    for etime in dataEnd: 
#        print stime,etime
#        #why are there data overlaps?
#        string = dataloc + net + '_' + sta + '/' + \
#            str(stime.year) + '/*' + str(stime.julday).zfill(3)+\
#            '/*'+ chan + '*'+comp+'*.seed'
#
#        #print(string)
#        fileName = glob.glob(string)
#        #print(string+ '/*'+ chan + '*'+comp+'*.seed')
#        #print(fileName)
#        
#        #print("Files is this long: "+str(len(files)))
#
## needed: from obspy.core import * for the following line to work
#        for curfile in fileName:
#            try:
#                #print('trying to read in file: '+ str(curfile))
#                st += read(curfile, starttime=stime, endtime=etime)
#            except:
#                continue
#                #if debug:
#                #print( 'Unable to get data ' + str(fileName))
###st.merge(fill_value='latest')
##st.plot()
##if debug:
##        print 'We have data'
#####return st

#!/bin/env python

#def getdata(net, sta, eventtime, lents, debug=False):
#    """
#        This function goes to both archives and gets the data.
#        At ASL the archives are located in:
#            /tr1/telemetry_days
#          or
#           /msd
#        depending on how long since the event passed.
#        from Adam Ringler
#    """

from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy.taup import TauPyModel
from obspy import read
import glob

# event time - this can be calculate based on the p-wave arrival
# this is for an event in Bolivia

eventTime = UTCDateTime("2017-02-21T14:09:04.000")
pWaveArrTime = 652
stime = eventTime+pWaveArrTime
etime = stime+60

evMag = 6.5
evDepth = 597.9
evLat = -19.284
evLon = 63.899

stLat = 34.945910
stLon = -106.457200
stDepth = -1820

net = "IU"
sta = "ANMO"
chan = "00"
comp = "BH*"
debug="True"

# Current default is LH add BH later
chan = 'BH*'

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
                    str(year) + '/' + str(day).zfill(3) + \
                    '/*'+ chan + '*.seed'
            print(string)
            #string = glob.glob(string)
            #print(string)
            #print(string)
            #files += glob.glob(string)
if debug:
    print(files)
#st = Stream()
for curfile in files:
#    try:
    print('trying to read in file: '+ curfile)
    st = read(curfile)
# in regular python I can get this to work... but I don't understand why it is not working here
# from obspy import read
#st = read('/msd/IU_ANMO/2017/052/*BH**.seed')
# are the quotes missing without the glob.glob expansion?  but I was having problems with Adam's
# st += read(curfile)... which may go away if this is a function def again.  It could be the 
# standalone case that is the problem.  I could really use Austin!
    print(stime)
#        st += read(curfile, starttime=stime, endtime=etime)
#    except:
#        if debug:
#        print 'Unable to get data ' + curfile
##st.merge(fill_value='latest')
st.plot()
if debug:
        print 'We have data'
#return st

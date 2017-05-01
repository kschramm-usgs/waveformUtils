#!/bin/env python

from obspy import UTCDateTime
from obspy.core import *
import glob

stime=UTCDateTime('2017-02-18T12:20:54.656944Z')
etime=UTCDateTime('2017-02-18T12:22:04.656944Z')

station = "ANMO"
channel = "00"
component = "BH"
net = "IU"
dataloc="/msd/"

st = Stream()

string = dataloc + net + '_' + station + '/' + \
         str(stime.year) + '/*' + str(stime.julday).zfill(3)+\
         '/*' + channel + '*' + component + '*.seed'

fileName=glob.glob(string)

for curfile in fileName:
    try:
        st += read(curfile,starttime=stime,endtime=etime)

    except:
        print('Unable to open file: '+ curfile)

st.plot()

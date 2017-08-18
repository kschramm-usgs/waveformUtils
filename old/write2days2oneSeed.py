#!/bin/env python


from obspy import UTCDateTime
from obspy.core import *
from obspy import read
import glob

""" reads in seed file, cuts to start/end time and writes out a new filei
    with cut in the name.

    would be nice to implement this with command line arguments.

    Kimberly Schramm
"""
stime=UTCDateTime('2017-166T22:46:00.0Z')
etime=UTCDateTime('2017-167T02:54:00.0Z')

print(stime.day)

network = "XX"
station = "MOFO"
channel = "50"
component = "BHZ"
prefix = 'LF'

dataloc="/tr1/telemetry_days/"

st = Stream()
fileName = []

#create file name
string1 = dataloc + network + '_' + station + '/' + str(stime.year) + '/*' \
         + str(stime.year) + '_' + str(stime.julday).zfill(3)+\
         '/*' + channel + '*' + component + '*.seed'

print(string1)
fileName=glob.glob(string1)

#need to read in stream for another day:
if stime.day != etime.day:
    string = dataloc + network + '_' + station + '/' + str(etime.year) + '/*' \
             + str(etime.year) + '_' + str(etime.julday).zfill(3)+\
             '/*' + channel + '*' + component + '*.seed'
    print(string) 
    fileName.append(glob.glob(string))

for curfile in fileName:
    try:
#        st += read(curfile,starttime=stime,endtime=etime)
        print(curfile)
        st += read(curfile)


    except:
        #maybe the exception could look for data on msd?
        print('Unable to open file: '+ str(curfile))

st.plot()
fileName=prefix+"_"+station+"_"+channel + "_" + component +".512.cut.seed"
print(fileName)
st.write(fileName,format='MSEED',reclen=512)

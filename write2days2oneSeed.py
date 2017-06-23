#!/bin/env python


from obspy import UTCDateTime
from obspy.core import *
from obspy import read
import glob

stime=UTCDateTime('2017-166T22:46:00.0Z')
etime=UTCDateTime('2017-167T02:52:00.0Z')

print(stime.day)

network = "XX"
station = "MOFO"
channel = "50"
component = "BHZ"
prefix = 'LF'

dataloc="/tr1/telemetry_days/"
#    /tr1/telemetry_days/XX_FBA1/2017/2017_151

st = Stream()
fileName = []

string1 = dataloc + network + '_' + station + '/' + str(stime.year) + '/*' \
         + str(stime.year) + '_' + str(stime.julday).zfill(3)+\
         '/*' + channel + '*' + component + '*.seed'

print(string1)
fileName=glob.glob(string)
#need to read in stream for another day:

if stime.day != etime.day:
    string = dataloc + network + '_' + station + '/' + str(etime.year) + '/*' \
             + str(etime.year) + '_' + str(etime.julday).zfill(3)+\
             '/*' + channel + '*' + component + '*.seed'
    print(string) 
    fileName.append(glob.glob(string))

for curfile in fileName:
    try:
        st += read(curfile,starttime=stime,endtime=etime)
#        st += read(curfile)


    except:
        print('Unable to open file: '+ str(curfile))

st.plot()
fileName=prefix+"_"+station+"_"+channel + "_" + component +".512.cut.seed"
print(fileName)
st.write(fileName,format='MSEED',reclen=512)

#!/bin/env python


from obspy import UTCDateTime
from obspy.core import *
from obspy import read
import glob

stime=UTCDateTime('2017-145T21:54:00.0Z')
etime=UTCDateTime('2017-145T22:08:00.0Z')
print(stime)

network = "GS"
station = "ASL9"
channel = "CB"
component = "BC0"
prefix = 'TG'

dataloc="/tr1/telemetry_days/"
#    /tr1/telemetry_days/XX_FBA1/2017/2017_151

st = Stream()

string = dataloc + network + '_' + station + '/' + str(stime.year) + '/*' \
         + str(stime.year) + '_' + str(stime.julday).zfill(3)+\
         '/*' + channel + '*' + component + '*.seed'

print(string)
fileName=glob.glob(string)

for curfile in fileName:
    try:
        st += read(curfile,starttime=stime,endtime=etime)
#        st += read(curfile)

    except:
        print('Unable to open file: '+ curfile)

st.plot()
fileName=prefix+"_"+station+"_"+channel + "_" + component +".512.cut.seed"
print(fileName)
st.write(fileName,format='MSEED',reclen=512)

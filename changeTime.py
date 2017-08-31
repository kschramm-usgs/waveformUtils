#!/bin/env python


from obspy import UTCDateTime
from obspy.core import *
from obspy import read
import glob

stime=UTCDateTime('2017-242T13:38:00.0Z')
etime=UTCDateTime('2017-242T13:53:00.0Z')

print(stime.julday)
print(etime.julday)
    

network = "XX"
station = "TPNV"
channel = "CB"
component = "BC0"
prefix = 'HF'

dataloc="/tr1/telemetry_days/"
#    /tr1/telemetry_days/XX_FBA1/2017/2017_151

fileName = []
for year in range(stime.year, etime.year+1):
    for day in range(stime.julday, etime.julday+1):
        string = dataloc + network + '_' + station + '/' + str(year) + '/*' \
                 + str(year) + '_' + str(day).zfill(3)+\
                 '/*' + channel + '*' + component + '*.seed'
        print(string)
        fileName += glob.glob(string)

st = Stream()
for curfile in fileName:
    try:
        if stime.julday != etime.julday:
            print('reading in file: '+curfile)
            st += read(curfile)
        else:
            st += read(curfile,starttime=stime,endtime=etime)
#        st += read(curfile)
    except:
        print('Unable to open file: '+ str(curfile))

if stime.julday != etime.julday:
    st2=st.copy()
    st2.merge(fill_value='latest')
    st2.trim(starttime=stime,endtime=etime)
    st2.plot()
    st = st2

st.plot()
:q


fileName=prefix+"_"+station+"_"+channel + "_" + component +".512.cut.seed"
print(fileName)
st.write(fileName,format='MSEED',reclen=512)

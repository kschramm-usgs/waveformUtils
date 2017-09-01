#!/bin/env python


from obspy import UTCDateTime
from obspy.core import *
from obspy import read
import glob
from obspy.mseed.util import shift_time_of_file

stime=UTCDateTime('2017-242T13:38:00.0Z')
etime=UTCDateTime('2017-242T13:53:00.0Z')

print(stime.julday)
print(etime.julday)
    

network = "XX"
station = "TPNV"
channel = "CB"
component = "BC0"
prefix = 'HF'
other='shifted'
cut='cut'

fileIn=prefix+"_"+station+"_"+channel + "_" + component +".512."+cut+".seed"
fileOut=prefix+"_"+station+"_"+channel + "_" + component +".512."+other+".seed"

shift_time_of_file(fileIn, fileOut, 10000)

st = read(fileOut)
st.plot()
tr=st[0]
st.write(fileOut,format="MSEED")

print(tr.stats.starttime)

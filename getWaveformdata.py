#!/bin/env python

''' 
Routine to get waveform data from IRIS given network and station
and event information
'''

from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy.taup import TauPyModel

# set the client where you want to retrieve the data
client = Client("IRIS")

# event time - this can be calculate based on the p-wave arrival
# this is for an event in Bolivia
eventTime = UTCDateTime("2017-02-21T14:09:04.000")
pWaveArrTime = 652
t = eventTime+pWaveArrTime
evMag = 6.5
evDepth = 597.9
evLat = -19.284
evLon = 63.899

stLat = 34.945910
stLon = -106.457200
stDepth = -1820

st = client.get_waveforms("IU", "ANMO", "00", "BHZ", t, t+60*60)
st.plot()


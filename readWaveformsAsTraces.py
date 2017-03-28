#!/bin/env python 

from obspy.core import trace
from obspy import read
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy.geodetics.base import locations2degrees
from obspy.geodetics.base import gps2dist_azimuth
from obspy.taup import TauPyModel

client = Client("IRIS")

# this is a deep earthquake in bolivia
t = UTCDateTime("2017-02-21T14:09:04")
eventTime = UTCDateTime("2017-02-21T14:09:04")
eventLat=-19.281
eventLon=-63.905
eventDepth = 597.

inventory = client.get_stations(network="IU", station="*", starttime=t)
model = TauPyModel(model="iasp91")

# to plot up all the stations...
#inventory.plot()

# to get the station coordinates
station_coordinates = []
for network in inventory:
    for station in network:
        station_coordinates.append((network.code, station.code, 
                                    station.latitude, station.longitude, 
                                    station.elevation))


for station in station_coordinates:        
    DegDist = locations2degrees(eventLat, eventLon,
                                station[2], station[3])
    StationAziExpec = gps2dist_azimuth(eventLat, eventLon,
                                       station[2], station[3])
    arrivals = model.get_travel_times(source_depth_in_km = eventDepth,
                                      distance_in_degree=DegDist,
                                      phase_list = ["P"])
    if DegDist > 25 and DegDist < 90:

        arrTime=eventTime + arrivals[0].time    
        bTime=arrTime-200
        eTime=arrTime+300
        try:
            st = client.get_waveforms(station[0],station[1],"00","BH?",
                                      bTime,eTime,attach_response=True)
        except:
            print("No data for station "+station[1])
            continue        
# Break up the stream into traces to remove the gain, taper, demean, filter,etc
        BH1 = st[0]
        BH2 = st[1]
        BHZ = st[2]
  
        st[0] = BH1.remove_sensitivity()
        st[1] = BH2.remove_sensitivity()
        st[2] = BHZ.remove_sensitivity()
        st.plot()
    else:
        print("Station "+station[0]+" does not have P arrival.")
    

        

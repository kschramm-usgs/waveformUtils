#!/bin/env python

def buildStationList(net,sta,cha,t,resp):
    '''This will build a list of stations for a given network.
       ex: staList = buildStationList("IU","*","BH*",eventTime,True) for resp info
       ex: staList = buildStationList("IU","*","BH*",eventTime,False) w/o resp info

    '''


    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime

    client = Client("IRIS")

# set some event info
# this is a deep earthquake in bolivia
#t = UTCDateTime("2017-02-21T14:09:04")

    if resp:
        inventory = client.get_stations(network="IU", station="*", starttime=t, 
                                        channel="BH*", level="response")
    else:
        inventory = client.get_stations(network="IU", station="*", starttime=t)

# to plot up all the stations...
    #inventory.plot()

# to get the station coordinates
    #station_coordinates = []
    #for network in inventory:
    #    for station in network:
    #        station_coordinates.append((network.code, station.code, station.latitude, station.longitude, station.elevation))
     
    return inventory;

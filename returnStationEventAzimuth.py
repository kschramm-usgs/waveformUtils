#!/bin/env python

from obspy.geodetics.base import locations2degrees
from obspy.geodetics.base import gps2dist_azimuth
# for vmqc001 you need the import below.
#from obspy.core.util import locations2degrees

staLat = 34.945910 # default station is ANMO
staLon = -106.4572 
#staLat = 51.882130
#staLon = -176.684

#eqLat = 37.580 #default event in Turkey, 2017055 11:07:27, M5.6
#eqLon = 38.440
#eqLat = 13.828
#eqLon = -92.269
eqLat = -19.281
eqLon = -63.905

# get the distance between the earthquake and station in degrees
DegDist = locations2degrees(staLat, staLon, eqLat, eqLon)


# get the station azimuth, back az and distance in meters...
StatAzim = gps2dist_azimuth(eqLat, eqLon, staLat, staLon)


# print the result
print 'The distance between the station and earthquake is: '+str(DegDist)
print 'The azimuth between the station and earthquake is: '+str(StatAzim[1])
print 'The azimuth between the earthquake and station is: '+str(StatAzim[2])

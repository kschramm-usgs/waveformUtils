#!/bin/env python
def getPwaveArrival(depth, distance):
    ''' Routine to calculate phase arrivals 
        example:
        getPhaseInfo(600,60,"P",False)
    '''
    from obspy.taup import TauPyModel

#specify earth model
    model = TauPyModel(model="iasp91")

# the source - receiver distance in degrees
#distance = 67.62
#distance = 45
#distance = 75.73
# the source depth in km
    #depth = 500
    #depth = 37.5
# list of phases you are interested in
    phaseList = ["P"]

    arrivals = model.get_travel_times(source_depth_in_km=depth,
                                  distance_in_degree=distance,
                                  phase_list=phaseList)

# to get the travel time for a phase...
    arr = arrivals[0] 
    pTime=arr.time
    print "The pwave arrives at: "+str(pTime)
    return pTime

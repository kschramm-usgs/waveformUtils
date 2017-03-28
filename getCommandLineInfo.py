#!/bin/env python
""" This will take information from the user about events
Much of this is grabbed from the get args function in Adam Ringler's
syncomp.py.  Reusing this also keeps the flags cohesive throughout 
applications at ASL
"""

import sys
import argparse


def getargs():
    """ Grab command line arguments to run synthetics. """
    parser = argparse.ArgumentParser(description = "Program to compare long-period event synthetics to data")

    parser.add_argument('-resDir',type=str, action = "store",
                        dest="resDir", required=True,
                        help="Result directory name Example: blah")

    parser.add_argument('-eventTime', type=str, action = "store",
                         dest="eventTime", required=True,
                         help="Enter a UTC time, ie: 2017-02-21T14:09:04")

    parser.add_argument('-eventLoc',type=str, action = "store",
                         dest="eventLoc", required=True, nargs='*',
                         default =['-19.284','-63.899','597'],
                         help="Enter the lat, lon, depth for the event")

#    parser.add_argument('-dir', type=str, action="store",
#                         dest="dir", required=True, nargs="+",
#                         help="Directory location Example: " + \
#                              "/home/user/put_stuff_here")

    parser.add_argument('-n', type=str, action="store",
                         dest = "network", required=True,
                         help="Network name Example: IU")

    parser.add_argument('-sta', type=str, action="store",
                        dest="sta", required = False,
                        help="Stations to use. Example with a \
                                comma (,) separator : TUC,ANMO")

    parser.add_argument('-cha', type=str, action="store",
                        dest="cha", required = False,
                        help="Channels to use. Example: BH*")

#    parser.add_argument('-tslen', type=int, action="store",
#                        dest="lents", required=False, default=4000.,
#                        help="Length of time series in seconds. \
#                                Example:  4000, default is 4000 s")

#    parser.add_argument('-debug', action="store_true", dest="debug",
#                        default=False, help="Run in debug mode")

#    parser.add_argument('-filter', action="store", nargs=3, dest="filter", required=False,
#                         default = [ 100, 200, 4],
#                         help="Filter parameters using minimum period,\
#                                 maximum period and number of corners.\
#                                 Example: 100 200 4, " + \
#                                 "default is 100 400 2")

    parserval=parser.parse_args()
    return parserval

# simple test of the system arguments:

print 'Number of arguments: ', len(sys.argv), ' arguments' 
print 'Argument List: ', str(sys.argv) 

parserval = getargs()
print eventLoc
eventLat = parserval.eventLoc[0]

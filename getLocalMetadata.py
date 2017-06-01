#!/bin/env python
''' a function to use local resp information '''
import re
from obspy.io.xseed import Parser
import os
# need to look at the dataless seed to get the station orientation.

#here is a snippet from austin:
fname = 'IU.dataless'
src = '/APPS/metadata/SEED/'
if re.search('dataless',fname):
    string = os.path.join(src,fname)
    print(string)
    sf=Parser(os.path.join(src,fname))
    #print(sf)
    inv=sf.getInventory()
    netsta=inv['stations'][0]['station_id']
    print (netsta)

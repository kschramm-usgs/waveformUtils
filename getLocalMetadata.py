#!/bin/env python
''' a function to use local resp information '''

# need to look at the dataless seed to get the station orientation.

#here is a snippet from austin:
if re.search('Dataless*',fname):
    sf=xseed.Parser(os.path.join(src,fname))
    inv=sf.getInventory()
    netsta=inv['stations'][0]['station_id']

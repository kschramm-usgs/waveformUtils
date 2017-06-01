#!/bin/env python

def getTR1data(station,network,channel,component,stime,etime):
    ''' This function returns a stream from /msd '''

    from obspy import UTCDateTime
    from obspy.core import *
    import glob

    #stime=UTCDateTime('2017-02-18T12:20:54.656944Z')
    #etime=UTCDateTime('2017-02-18T12:22:04.656944Z')
    #
    #station = "ANMO"
    #channel = "00"
    #component = "BH"
    #network = "IU"

    dataloc="/tr1/telemetry_days/"
#    /tr1/telemetry_days/XX_FBA1/2017/2017_151

    st = Stream()

    string = dataloc + network + '_' + station + '/' + str(stime.year) + '/*' \
             + str(stime.year) + '_' + str(stime.julday).zfill(3)+\
             '/*' + channel + '*' + component + '*.seed'

    print(string)
    fileName=glob.glob(string)

    for curfile in fileName:
        try:
            st += read(curfile,starttime=stime,endtime=etime)

        except:
            print('Unable to open file: '+ curfile)

    return st

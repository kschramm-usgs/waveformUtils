#!/bin/env python

from obspy.core import read, UTCDateTime

st = read('/home/kschramm/java/asl_sensor_suite/data/random_cal_3/CB_BC0.512.seed')
if (st.getGaps()):
    print('data has gaps')
    st.printGaps()


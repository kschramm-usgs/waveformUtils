#!/bin/env python

from obspy.core import read, UTCDateTime

st = read('/msd/IU_CCM/2017/151/*EHZ*')
if (st.get_gaps()):
    print('data has gaps')
    st.print_gaps()


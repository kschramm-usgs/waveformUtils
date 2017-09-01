#!/bin/env python

import obspy.core
import matplotlib.pyplot as plt
import obspy
import numpy as np


out_stream1 = obspy.read('/home/kschramm/java/asl_sensor_suite/data/MAJO_data/HF_MAJO_10_EHZ.512.cut.seed')
out_stream2 = obspy.read('/home/kschramm/java/asl_sensor_suite/data/TPNV/HF_TPNV_00_EHZ.512.cut.seed')
out_trace1 = out_stream1[0]
out_trace2 = out_stream2[0]

#normalize the traces
normtrace1 = out_trace1.copy()
normtrace2 = out_trace2.copy()
normtrace1.normalize()
normtrace2.normalize()


plt.subplot(4,1,1)
plt.plot(out_trace1.data,'r',label=out_trace1.stats['station'])
plt.legend()

plt.subplot(4,1,2)
plt.plot(out_trace2.data,'b',label=out_trace2.stats['station'])
plt.legend()

plt.subplot(4,1,3)
plt.plot(out_trace1.data,'r',label=out_trace1.stats['station'])
plt.plot(out_trace2.data,'b',label=out_trace2.stats['station'])
plt.legend()

plt.subplot(4,1,4)
plt.plot(normtrace1.data,'r',label=out_trace1.stats['station'])
plt.plot(normtrace2.data,'b',label=out_trace2.stats['station'])
plt.ylabel('norm(amp)')
plt.legend()

plt.show()



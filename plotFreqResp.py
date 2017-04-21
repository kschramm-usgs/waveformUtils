import numpy as np
import matplotlib.pyplot as plt

from obspy.signal.invsim import paz_to_freq_resp
from response import Response

pol=[-0.01234-1j*0.01234, -0.01234+1j*0.01234, -39.18-1j*49.12, -39.18+1j*49.12]
zer=[0 , 0]

# use Austin's response class to build the resp from the poles and zeros
inst = Response(desc='STS-5/360',units='Radians')
inst.zeros = zer
inst.poles = pol
norm_freq=1.0
n,f = inst.check_normalization(freq=norm_freq, nfft=2**26,t_sample=0.001)
scale_fac= 1.0/n
print ('The A0 norm factor is: '+str(scale_fac))


#poles = [-4.440 + 4.440j, -4.440 - 4.440j, -1.083 + 0.0j]
#zeros = [0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]
scale_fac = 0.4

h, f = paz_to_freq_resp(inst.poles, inst.zeros, scale_fac, 0.001, 2**26, freq=True)

plt.figure()
plt.subplot(121)
plt.loglog(f, abs(h))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')

plt.subplot(122)
# take negative of imaginary part
phase = np.unwrap(np.arctan2(-h.imag, h.real))
plt.semilogx(f, phase)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [radian]')
# title, centered above both subplots
plt.suptitle('Frequency Response of '+inst.desc +' Seismometer')
# make more room in between subplots for the ylabel of right plot
plt.subplots_adjust(wspace=0.3)
plt.show()


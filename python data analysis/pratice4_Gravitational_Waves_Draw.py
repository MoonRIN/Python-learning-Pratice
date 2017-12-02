import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate_h, hstrain = wavfile.read(r"H1_Strain.wav", "rb")
rate_l, lstrain = wavfile.read(r"L1_Strain.wav", "rb")
reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose()

htime_interval = 1/rate_h
ltime_interval = 1/rate_l
fig = plt.figure(figsize=(12, 6))

htime_len = hstrain.shape[0]/rate_h
htime = np.arange(-htime_len/2, htime_len/2, htime_interval)
plth = fig.add_subplot(221)
plth.plot(htime, hstrain, 'y')
plth.set_xlabel('Time(Second)')
plth.set_ylabel('H1_Strain')
plth.set_title('H1 Strain')

ltime_len = lstrain.shape[0]/rate_l
ltime = np.arange(-ltime_len/2, ltime_len/2, ltime_interval)
pltl = fig.add_subplot(222)
pltl.plot(ltime, lstrain, 'g')
pltl.set_xlabel('Time(second)')
pltl.set_ylabel('L1_Strain')
pltl.set_title('L1_Strain')

pltref = fig.add_subplot(212)
pltref.plot(reftime, ref_H1)
pltref.set_xlabel('Time(Sceond)')
pltref.set_ylabel('Ref_Strain')
pltref.set_title('Ref_Strain')

plt.savefig("Gravitational_Waves.png")
plt.show()
plt.close(fig)
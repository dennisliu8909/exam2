import matplotlib.pyplot as plt
import numpy as np
import serial
import time

Fs = 32.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0, 31) # time vector; create Fs samples between 0 and 1.0 sec.
y = np.arange(0, 31) # signal vector; create Fs samples

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # a vector of frequencies; two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev)
for x in range(0, int(Fs)):
    line=s.readline() # Read an echo string from B_L4S5I_IOT01A terminated with '\n'
    # print line
    y[x] = float(line)

if y != 2:
    Y = 1
else:
    Y = 0

fig, ax = plt.subplots(2, 1)
ax[0].plot(x,y)
ax[0].set_xlabel('sample')
ax[0].set_ylabel('classified gesture')

ax[1].plot(x,Y) # plotting the spectrum
ax[1].set_xlabel('sample')
ax[1].set_ylabel('feature')
plt.show()
s.close()
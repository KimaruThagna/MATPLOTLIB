import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anime
from matplotlib import style
style.use('dark_background')
# Sine wave is given by Amplitude=sin(frequencyxtime)
#animation based on varying the size of the main list(time array) by increasing its boundary after every loop
# for x in range(1,20,1):
#
#     time=np.arange(0,x,0.1) # create an ndarray(n-dimensional array) of values from 0 to 10 at intervals of 0.1
#     CosAmplitude=np.cos(time)
#     plt.pause(1)
#     plt.clf()
#     plt.plot(time,CosAmplitude)
#     plt.title('SINE WAVE')
#     plt.xlabel('Radians')
#     plt.axhline(y=0, color='k')
#     plt.ylabel('AMPLITUDE=SIN(TIME)')
#     plt.grid(True,which='both')
# plt.show()

# animation based on feeding the main lists(xs,ys) periodically
xs=[]
ys=[]
time=np.arange(0,10,0.1)
for i in range(len(time)):
    Interimtime=time[i]
    xs.append(Interimtime)
    ys.append(np.sin(Interimtime))
    plt.pause(0.1)
    plt.clf()
    plt.plot(xs,ys)
    plt.title('SINE WAVE t='+str(i/10))
    plt.xlabel('Radians')
    plt.axhline(y=0, color='w')
    plt.xlim(0,10)
    plt.ylim(-1.50,1.50)
    plt.ylabel('AMPLITUDE=SIN(TIME)')
    plt.grid(True,which='both')
plt.show()



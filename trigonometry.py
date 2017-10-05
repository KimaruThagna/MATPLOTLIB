import matplotlib.pyplot as plt
import numpy as np
# Sine wave is given by Amplitude=sin(frequencyxtime)
time=np.arange(0,10,0.1) # create an ndarray(n-dimensional array) of values from 0 to 10 at intervals of 0.1
Amplitude=np.sin(time)
CosAmplitude=np.cos(time)
plt.plot(time,CosAmplitude)
plt.title('SINE WAVE')
plt.xlabel('Radians')
plt.ylabel('AMPLITUDE=SIN(TIME)')
plt.axhline(y=0,color='k')
plt.grid(True,which='both')
plt.show()
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
# 3D data
x=[1,2,3,4,5,6,7,8,9,10]
y=[7,4,1,8,5,2,9,6,3,1]
z=np.zeros(10)
#d dimensions are for depth in the specific axes
dx=np.ones(10) # depth long x
dy=np.ones(10)# depth along Y
dz=[1,2,3,4,5,6,7,8,9,20]# depth along Z

ax1.bar3d(x,y,z,dx,dy,dz)
ax1.set_xlabel('x-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')
plt.show()
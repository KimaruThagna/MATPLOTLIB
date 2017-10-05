from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
# 3D data
x=[3,2,1,4,7,8,9,5,4,1]
y=[1,2,4,7,8,5,6,3,0,1]
z=[1,2,4,4,5,8,9,5,4,10]

x2=[-3,-2,-1,-4,-7,-8,-9,-5,-4,-1]
y2=[-1,-2,-4,-7,-8,-5,-6,-3,-4,-1]
z2=[1,2,4,4,5,8,9,5,4,10]
#ax1.plot_wireframe(x,y,z) # 3d plotting
ax1.scatter(x,y,z,c='g',marker='o')
ax1.scatter(x2,y2,z2,c='r',marker='o')
ax1.set_xlabel('x-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')
plt.show()
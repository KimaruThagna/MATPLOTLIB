import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab

mp.rcParams['xtick.direction']='out'
mp.rcParams['ytick.direction']='out'
delta=0.025
x=np.arange(-3.0,3.0,delta)
y=np.arange(-2.0,2.0,delta)
x,y=np.meshgrid(x,y)
z1=mlab.bivariate_normal(y,y,1.0,1.0,0.0,0.0)
z2=mlab.bivariate_normal(y,y,1.5,0.5,1,1)
#difference of gaussians
z=10.0*(z2-z1)
# the clable arguments control whether the labels are drawn over the line segments or removing the line underneath
plt.figure()
cs=plt.contour(x,y,z)
plt.clabel(cs,inline=1,fontsize=10)
plt.title('DEFAULT WITH LABELS')
#using a colormap to specify colors
im=plt.imshow(z,interpolation='bilinear',origin='lower',cmap=cm.gray,extent=(-3,3,-2,2))
levels=np.arange(-1.2,1.6,0.2)
cs=plt.contour(z,levels,origin='lower',extent=(-3,3,-2,2),linewidths=2)
#thicken zero contour
zc=cs.collections[6]
plt.setp(zc,linewidth=4)
cb=plt.colorbar(cs,shrink=0.8,extend='both')
plt.show()

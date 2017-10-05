import matplotlib.pyplot as plt
import random
from matplotlib import style
style.use('fivethirtyeight')
fig=plt.figure()

def create_plots():
    xs=[]
    ys=[]
    for i in range(10):
        xs.append(i)
        ys.append(random.randrange(10))
    return xs,ys
#method 1
# ax1=fig.add_subplot(221) #along the y axis, support two plots, along x axis support 2 plot...plot number 1
# ax2=fig.add_subplot(222) #along the y axis, support two plots, along x axis support 2 plot...plot number 2
# ax3=fig.add_subplot(212)

ax1=plt.subplot2grid((6,1),(0,0),rowspan=1,colspan=1) #6,1 gives the size of the grid(6 rows 1 column) 0,0 gives the starting point or origin of grid
ax2=plt.subplot2grid((6,1),(1,0),rowspan=4,colspan=1) # rowspan gives how many rows your axes will go, colspan-how many columns
ax3=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1)

x=[1,2,3,4]
y=[1,2,3,4]
ax1.plot(x,y)

x,y=create_plots()
ax2.plot(x,y)

x,y=create_plots()
ax3.plot(x,y)
plt.grid(True,which='both')
plt.show()
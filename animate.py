import  matplotlib.pyplot as plt
import matplotlib.animation as anime
from matplotlib import style
style.use('fivethirtyeight')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
    #from here
    graphData=open('data','r').read()
    lines=graphData.split('\n') # split the data in the text file at every newline
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:   #ensures you dont process a blank line ege at end of document
            x,y=line.split(',') #each line is split by the comma and the first chunk goes to x, the second to y
            xs.append(x)
            ys.append(y)
            #to here
            #all this can be replaced with x,y=np.loadtxt('data',delimiter=',',unpack=True)
    ax1.clear()
    ax1.plot(xs,ys)

an=anime.FuncAnimation(fig,animate,interval=500) # te function takes the figure to animate, the animation function and time in milliseconds
plt.show()
import matplotlib.pyplot as plt
x=[2,4,6,8]
y=[10,4,8,7]
x2=[1,2,3,4]
y2=[10,22.1,1,0.5]
x3=[2,3,5,7]
y3=[1,6,8,7]
plt.bar(x,y,label='Series 1',color='black')# plots a bar chart
plt.bar(x3,y3,label='Series 3',color='green')# plots a bar chart
plt.plot(x2,y2,label='Series 2')
plt.title('ALPHA\n TEST')
plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.legend()
plt.show()
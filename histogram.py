import matplotlib.pyplot as plt
ages=[12,45,6,55,12,3,45,23,43,21,99,67,8,9,67,44,34,32,30,20,76,77,100,127,102,103]
bins=[x for x in range(0,140,10) ] # start at 0 end at 140(exclusive) and go in leaps of 10
plt.hist(ages,bins,histtype='bar',rwidth=0.8,label='Histogram',color='grey')
plt.title('ALPHA\n TEST')
plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.legend()
plt.show()

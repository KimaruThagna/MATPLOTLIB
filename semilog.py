import matplotlib.pyplot as plt
import numpy as np
# A semilog graph..data on ne scale is logarithimic(exponential increase) and on the other scale is linear
# used to depict data with very large disparity between the large amd small values eg exponential growth
hours=[1,2,3,4,5,6,7,8]
population=[2000,2500,18000,120000,190000,200000,500000,1000000]# population of bacteria at every hour
#display grid
plt.grid(True,which='both')
# a xis..linear scale,,Y axis,,logarithmic scale
plt.semilogy(hours,population)
plt.ylim(2000,1500000)
plt.xlim(0,10)
plt.title('BACTERIA POPULATION GROWTH')
plt.xlabel('HOURS')
plt.ylabel('POPULATION IN MILLIONS')
plt.show()


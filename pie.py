import matplotlib.pyplot as plt
# explode is a tuple which is equal to the number of pies in the chart
# it holds values which define how far from the center a wedge is
Xplode=(0.1,0.0,0.0,0.1,0.1,0.0)
labels=['Asia','Europe','Africa','N-America','S-America','Australia']
population=[12.2,14.55,10,44.12,20.24,33.21]
figureObject,axesObject=plt.subplots()
axesObject.pie(population,labels=labels,explode=Xplode,autopct='%1.2f',startangle=90,shadow=True,frame=True)
#autopct gives the format of the values to be displayed
axesObject.axis('equal') # aspect ratio being equal makes the pie be an upright circle
plt.show()


import matplotlib.pyplot
import numpy

backLegSensorValues=numpy.load("data/backLegSensorValues.npy")
#print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)

frontLegSensorValues=numpy.load("data/frontLegSensorValues.npy")
#print(frontLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)

matplotlib.pyplot.show()
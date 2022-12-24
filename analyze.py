import matplotlib.pyplot
import numpy

backLegSensorValues=numpy.load("data/backLegSensorValues.npy")
#print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg Sensor", linewidth=3)

frontLegSensorValues=numpy.load("data/frontLegSensorValues.npy")
#print(frontLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg Sensor")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
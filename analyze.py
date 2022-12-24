import matplotlib.pyplot
import numpy

#backLegSensorValues=numpy.load("data/backLegSensorValues.npy")
#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg Sensor", linewidth=3)

#frontLegSensorValues=numpy.load("data/frontLegSensorValues.npy")
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg Sensor")

targetAngles=numpy.load("data/sinFunction.npy")
matplotlib.pyplot.plot(targetAngles, label="Front Leg Sensor")

#matplotlib.pyplot.legend()
matplotlib.pyplot.show()
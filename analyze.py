import matplotlib.pyplot
import numpy

#backLegSensorValues=numpy.load("data/backLegSensorValues.npy")
#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg Sensor", linewidth=3)

#frontLegSensorValues=numpy.load("data/frontLegSensorValues.npy")
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg Sensor")

backLegTargetAngles=numpy.load("data/backLegTargetAngles.npy")
matplotlib.pyplot.plot(backLegTargetAngles, label="Back Leg", linewidth=3)

frontLegTargetAngles=numpy.load("data/frontLegTargetAngles.npy")
matplotlib.pyplot.plot(frontLegTargetAngles, label="Front Leg")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
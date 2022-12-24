import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import matplotlib.pylab as plt
import random
import time

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues=numpy.zeros(1000)
frontLegSensorValues=numpy.zeros(1000)

backLegAmplitude=numpy.pi/4
backLegFrequency=10
backLegPhaseOffSet=-numpy.pi/4
backLegTargetAngles=[]

frontLegAmplitude=numpy.pi/4
frontLegFrequency=10
frontLegPhaseOffSet=0
frontLegTargetAngles=[]

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backLegTargetAngles.append(backLegAmplitude*numpy.sin(backLegFrequency*(i*numpy.pi/500)+backLegPhaseOffSet))
    frontLegTargetAngles.append(frontLegAmplitude*numpy.sin(frontLegFrequency*(i*numpy.pi/500)+frontLegPhaseOffSet))
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_BackLeg', controlMode=p.POSITION_CONTROL, targetPosition=(backLegTargetAngles[i]), maxForce=30)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_FrontLeg', controlMode=p.POSITION_CONTROL, targetPosition=(frontLegTargetAngles[i]), maxForce=30)
    time.sleep(1/3000)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
#numpy.save("data/backLegTargetAngles.npy", backLegTargetAngles)
#numpy.save("data/frontLegTargetAngles.npy", frontLegTargetAngles)

p.disconnect()
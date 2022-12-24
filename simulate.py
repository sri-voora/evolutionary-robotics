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

amplitude=numpy.pi/4
frequency=1
phaseOffSet=0
targetAngles=[]

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    targetAngles.append(numpy.sin((numpy.pi/-4)+(i*(numpy.pi/2000))))
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_BackLeg', controlMode=p.POSITION_CONTROL, targetPosition=(targetAngles[i]), maxForce=30)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_FrontLeg', controlMode=p.POSITION_CONTROL, targetPosition=(targetAngles[i]), maxForce=30)
    time.sleep(1/6000)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("data/sinFunction.npy", targetAngles)

#for x in range(10):
    #targetAngles=numpy.sin((1/6)*numpy.pi)
#print(targetAngles)

p.disconnect()
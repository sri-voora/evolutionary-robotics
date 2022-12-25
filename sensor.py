import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time

class SENSOR:
    def __init__(self, linkName):
        self.linkName=linkName
        self.values=numpy.zeros(1000)
        #print(self.values)
    
    def Get_Value(self, i):
        self.values[i]=pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
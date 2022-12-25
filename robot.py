import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.sensors={}
        self.motors={}

        
        self.robotId = p.loadURDF("body.urdf")
        self.nn=NEURAL_NETWORK("brain.nndf")
        
        pyrosim.Prepare_To_Simulate(self.robotId)
        
        self.PrepareToSense()
        self.PrepareToAct()

    def PrepareToSense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName]=SENSOR(linkName)
    
    def Sense(self,t):
        for sens in self.sensors:
            self.sensors[sens].Get_Value(t)
    
    def PrepareToAct(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName]=MOTOR(jointName)
    
    def Act(self, t):
        for mot in self.motors:
            self.motors[mot].Set_Value(self.robotId, t)
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()
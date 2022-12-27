import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID=solutionID
        self.sensors={}
        self.motors={}

        self.robotId = p.loadURDF("body.urdf")
        self.nn=NEURAL_NETWORK("brain"+str(self.solutionID)+".nndf")
        
        pyrosim.Prepare_To_Simulate(self.robotId)
        
        self.PrepareToSense()
        self.PrepareToAct()

        os.system("rm brain"+str(self.solutionID)+".nndf")

    def PrepareToSense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName]=SENSOR(linkName)
    
    def Sense(self,t):
        for sens in self.sensors:
            self.sensors[sens].Get_Value(t)
    
    def PrepareToAct(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName]=MOTOR(jointName)
            #print(jointName)
    
    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName_str=self.nn.Get_Motor_Neurons_Joint(neuronName)
                jointName=jointName_str.encode(encoding='UTF-8')
                desiredAngle=self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
    
    def Think(self):
        self.nn.Update()
        #self.nn.Print()
    
    def Get_Fitness(self):
        stateOfLinkZero=p.getLinkState(self.robotId, 0)
        positionOfLinkZero=stateOfLinkZero[0]
        xCoordinateOfLinkZero=positionOfLinkZero[0]
        
        fitnessFile=open("tmp"+str(self.solutionID)+".txt","w")
        os.system("mv tmp"+str(self.solutionID)+".txt fitness"+str(self.solutionID)+".txt")
        fitnessFile.write(str(xCoordinateOfLinkZero))
        fitnessFile.close()
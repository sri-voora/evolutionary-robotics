import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI):
        self.directOrGUI=directOrGUI
        if self.directOrGUI=="DIRECT":
            self.physicsClient=p.connect(p.DIRECT)
            #print("Is direct.")
        else:
            self.physicsClient=p.connect(p.GUI)
        #self.physicsClient=p.connect(p.DIRECT)
        self.world=WORLD()
        self.robot=ROBOT()

    def Run(self):
        for i in range(1000):
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            #time.sleep(1/10000)
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI=directOrGUI
        if self.directOrGUI=="DIRECT":
            self.physicsClient=p.connect(p.DIRECT)
        else:
            self.physicsClient=p.connect(p.GUI)

        self.solutionID=solutionID
        self.world=WORLD()
        self.robot=ROBOT(self.solutionID)

    def Run(self):
        for i in range(1000):
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            if self.directOrGUI=="GUI":
                time.sleep(1/4000)
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
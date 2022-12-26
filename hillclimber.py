import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import constants as c
import copy

from solution import SOLUTION

class HILL_CLIMBER:
    def __init__(self):
        self.parent=SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()
    
    def Spawn(self):
        self.child=copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
    
    def Print(self):
        print("Parent Fitness is: "+str(self.parent.fitness)+". Child Fitness is: "+str(self.child.fitness)+".")
    
    def Select(self):
        if (self.parent.fitness>=self.child.fitness):
            self.parent=self.child
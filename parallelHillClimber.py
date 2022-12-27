import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import constants as c
import copy
import os

from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #os.system("rm brain*.nndf")
        #os.system("rm fitness*.txt")

        self.nextAvailableID=0
        self.parents={}
        for p in range(c.populationSize):
            self.parents[p]=SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1

    def Evolve(self):
        #self.parent.Evaluate("GUI")
        
        #for parent in self.parents:
            #self.parents[parent].Start_Simulation("DIRECT")
        #for parent in self.parents:
            #self.parents[parent].Wait_For_Simulation_To_End()
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
    
    def Spawn(self):
        self.children={}
        for parent in self.parents.keys():
            self.children[parent]=copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID+=1
        #self.child=copy.deepcopy(self.parent)
        #self.child.Set_ID(self.nextAvailableID)
        #self.nextAvailableID+=1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()
        #self.child.Mutate()
    
    def Print(self):
        for key in self.parents.keys():
            print("\nParent Fitness is: "+str(self.parents[key].fitness)+". Child Fitness is: "+str(self.children[key].fitness)+".\n")
        #print("Parent Fitness is: "+str(self.parent.fitness)+". Child Fitness is: "+str(self.child.fitness)+".")
    
    def Select(self):
        for key in self.parents.keys():
            if (self.parents[key].fitness>=self.children[key].fitness):
                self.parents[key]=self.children[key]
        #if (self.parent.fitness>=self.child.fitness):
            #self.parent=self.child
    
    def Show_Best(self):
        bestParent=None
        bestParentFitness=100
        for parent in self.parents.keys():
            if self.parents[parent].fitness<=bestParentFitness:
                bestParent=self.parents[parent]
                bestParentFitness=self.parents[parent].fitness
        bestParent.Start_Simulation("GUI")
        #self.parent.Evaluate("GUI")
        #self.parent.Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for solution in solutions.keys():
            solutions[solution].Start_Simulation("DIRECT")
        for solution in solutions.keys():
            solutions[solution].Wait_For_Simulation_To_End()
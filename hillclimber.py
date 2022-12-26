import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time

from solution import SOLUTION

class HILL_CLIMBER:
    def __init__(self):
        self.parent=SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()
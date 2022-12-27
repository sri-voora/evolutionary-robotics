import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import matplotlib.pylab as plt
import random
import constants as c
import sys
from simulation import SIMULATION

directOrGUI=sys.argv[1]
solutionID=sys.argv[2]
simulation=SIMULATION(directOrGUI, solutionID)
#simulation=SIMULATION()
simulation.Run()
simulation.Get_Fitness()
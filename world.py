import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time

class WORLD:
    def __init__(self):
        self.physicsClient=p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
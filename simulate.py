import pybullet as p
physicsClient = p.connect(p.GUI)
for i in list(range(1,1001,1)):
    p.stepSimulation()
p.disconnect()
import pybullet as p
import time
physicsClient = p.connect(p.GUI)
for i in list(range(1,1001,1)):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()
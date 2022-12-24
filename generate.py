import pyrosim.pyrosim as pyrosim

x=0
y=0
z=0.5

length=1
width=1
height=1

pyrosim.Start_SDF("boxes.sdf")
for c in range(5):
    for r in range(5):
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[(x+c),(y+r),(z+i)], size=[(length*(0.9**i)),(width*(0.9**i)),(height*(0.9**i))])
pyrosim.End()
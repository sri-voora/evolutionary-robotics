import pyrosim.pyrosim as pyrosim

x=0
y=0
z=0.5

length=1
width=1
height=1

pyrosim.Start_SDF("boxes.sdf")
for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x,y,(z+i)], size=[length,width,height])
pyrosim.End()
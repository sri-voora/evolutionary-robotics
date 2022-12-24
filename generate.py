import pyrosim.pyrosim as pyrosim

x=0
y=0
z=1.5

length=1
width=2
height=3

pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
pyrosim.End()
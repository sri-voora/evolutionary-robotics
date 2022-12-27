import os
from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER

#for x in range(5):
    #os.system("python3 generate.py")
    #os.system("python3 simulate.py")

#hc=HILL_CLIMBER()
#hc.Evolve()
#hc.Show_Best()

os.system("rm brain*.nndf")
os.system("rm fitness*.txt")
os.system("python3 solution.py")
os.system("python3 parallelHillClimber.py")

phc=PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
#
# Student Name: <put your name here>
# Student ID  : <put your ID here>
#
# emoSim.py - simulation of emotions as peeple moev through a world
#
# Version information:
#    - 2026-03-30 - inital version supplied
# 
# Usage: 
#    <basic information to run program, more complete in README and User Guide
#
import numpy as np
import matplotlib.pyplot as plt
from peeple import Peep

def build_world(xmax, ymax):
    world = np.zeros((xmax, ymax), dtype="int")
    world[0,:] = 11
    world[-1,:] = 11
    world[:,0] = 11
    world[:,-1] = 11
    return world

def plot_world(world, plist, ax):
    xvalues = [p.get_pos()[0] for p in plist]
    yvalues = [p.get_pos()[1] for p in plist]
    ax.imshow(world.T, origin="lower")
    ax.scatter(xvalues, yvalues)

def get_subgrid(p, world):
    pos = p.get_pos()
    sgrid = world[pos[0]-1:pos[0]+2,pos[1]-1:pos[1]+2]
    return sgrid

SIMLENGTH = 1
WORLD_X = 30
WORLD_Y = 20

emo_world = build_world(WORLD_X, WORLD_Y)

peeps = []
p = Peep("Dora", (9,5))
peeps.append(p)

#plt.ion()

for t in range(SIMLENGTH):
    
    # move actors
    for peep in peeps:
        peep.step_change()   # add subgrid for validating moves
        
    # actor interations (later)

    # update emo_world (later)

    # plot current step
    #print(emo_world)
    fig, axes = plt.subplots(1, 1, figsize=(10,6))
    plot_world(emo_world, peeps, axes)
    #plot_world(emo_world, peeps, axes[0])


    plt.show()
    #plt.pause(1)
    #plt.clf()

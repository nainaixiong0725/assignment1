#
# Author:
# ID:
#
# emoSim.py - Basic emotion simulation
#

import random

import matplotlib.pyplot as plt
import numpy as np

from peeple import Peep


WORLD_X = 30
WORLD_Y = 20
NUM_PEEPS = 8
SIM_LENGTH = 10


def build_world(xmax, ymax):
    """Create a simple empty world grid."""
    world = np.zeros((xmax, ymax), dtype=int)
    return world


def make_peeps(num_peeps, xmax, ymax):
    """Create a list of Peep objects at random positions."""
    peeps = []

    for i in range(num_peeps):
        rand_x = random.randint(0, xmax - 1)
        rand_y = random.randint(0, ymax - 1)
        peep = Peep("Peep" + str(i), (rand_x, rand_y))
        peeps.append(peep)

    return peeps


def plot_world(world, peeps):
    """Plot the world and peep positions."""
    xvalues = []
    yvalues = []

    for peep in peeps:
        pos = peep.get_pos()
        xvalues.append(pos[0])
        yvalues.append(pos[1])

    plt.imshow(world.T, origin="lower", cmap="Pastel1")
    plt.scatter(xvalues, yvalues, color="red")
    plt.title("Emotion Simulation - Basic Movement")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.xlim(0, WORLD_X - 1)
    plt.ylim(0, WORLD_Y - 1)
    plt.show()


def main():
    """Run the basic emotion simulation."""
    world = build_world(WORLD_X, WORLD_Y)
    peeps = make_peeps(NUM_PEEPS, WORLD_X, WORLD_Y)

    print("### INITIAL PEEPS ###")
    for peep in peeps:
        print(peep)

    for step in range(SIM_LENGTH):
        print("\n### TIMESTEP", step, "###")
        for peep in peeps:
            peep.step_change(WORLD_X, WORLD_Y)
            print(peep)

    plot_world(world, peeps)


if __name__ == "__main__":
    main()

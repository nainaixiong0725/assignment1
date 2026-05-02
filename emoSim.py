import random

import matplotlib.pyplot as plt
import numpy as np

from peeple import Peep


WORLD_X = 30
WORLD_Y = 20
NUM_PEEPS = 8
SIM_LENGTH = 10


def build_world(xmax, ymax):
    """Create a world grid with some barrier cells."""
    world = np.zeros((xmax, ymax), dtype=int)

    # Add four square barriers in the world.
    world[1:4, 1:4] = 11
    world[1:4, ymax - 4:ymax - 1] = 11
    world[xmax - 4:xmax - 1, 1:4] = 11
    world[xmax - 4:xmax - 1, ymax - 4:ymax - 1] = 11

    return world


def make_peeps(num_peeps, world):
    """Create a list of Peep objects at random non-barrier positions."""
    peeps = []
    xmax = world.shape[0]
    ymax = world.shape[1]

    for i in range(num_peeps):
        rand_x = random.randint(0, xmax - 1)
        rand_y = random.randint(0, ymax - 1)

        # If a peep starts on a barrier, move it to the centre area.
        if world[rand_x, rand_y] == 11:
            rand_x = xmax // 2
            rand_y = ymax // 2

        peep = Peep("Peep" + str(i), (rand_x, rand_y))
        peeps.append(peep)

    return peeps


def get_average_emotions(peeps):
    """Calculate average happy, sad and angry values."""
    total_happy = 0
    total_sad = 0
    total_angry = 0

    for peep in peeps:
        total_happy += peep.happy
        total_sad += peep.sad
        total_angry += peep.angry

    avg_happy = total_happy / len(peeps)
    avg_sad = total_sad / len(peeps)
    avg_angry = total_angry / len(peeps)

    return avg_happy, avg_sad, avg_angry


def plot_world(world, peeps):
    """Plot the world, barriers and peep positions."""
    xvalues = []
    yvalues = []

    for peep in peeps:
        pos = peep.get_pos()
        xvalues.append(pos[0])
        yvalues.append(pos[1])

    plt.figure()
    plt.imshow(world.T, origin="lower", cmap="Paired", vmin=0, vmax=11)
    plt.scatter(xvalues, yvalues, color="red")

    plt.title("Emotion Simulation - Barriers")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.xlim(0, WORLD_X - 1)
    plt.ylim(0, WORLD_Y - 1)
    plt.show()


def plot_emotions(happy_history, sad_history, angry_history):
    """Plot average emotions over time."""
    timesteps = range(len(happy_history))

    plt.figure()
    plt.plot(timesteps, happy_history, label="Happy")
    plt.plot(timesteps, sad_history, label="Sad")
    plt.plot(timesteps, angry_history, label="Angry")

    plt.title("Average Emotions Over Time")
    plt.xlabel("Timestep")
    plt.ylabel("Average emotion value")
    plt.legend()
    plt.show()


def main():
    """Run the basic emotion simulation."""
    world = build_world(WORLD_X, WORLD_Y)
    peeps = make_peeps(NUM_PEEPS, world)

    happy_history = []
    sad_history = []
    angry_history = []

    print("### INITIAL PEEPS ###")
    for peep in peeps:
        print(peep)

    for step in range(SIM_LENGTH):
        print("\n### TIMESTEP", step, "###")
        for peep in peeps:
            peep.step_change(world)
            print(peep)

        avg_happy, avg_sad, avg_angry = get_average_emotions(peeps)
        happy_history.append(avg_happy)
        sad_history.append(avg_sad)
        angry_history.append(avg_angry)

    plot_world(world, peeps)
    plot_emotions(happy_history, sad_history, angry_history)


if __name__ == "__main__":
    main()

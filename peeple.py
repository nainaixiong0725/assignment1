#
# Author:
# ID:
#
# peeple.py - Class definitions for emotion simulation peeps
#

import random


class Peep:
    """A simple person in the emotion simulation."""

    moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.first = pos

        # Basic emotions for the assignment.
        self.happy = 50
        self.sad = 10
        self.angry = 10

    def __str__(self):
        return self.name + " @ " + str(self.pos)

    def get_pos(self):
        return self.pos

    def step_change(self, xmax, ymax):
        """Move the peep randomly by one square inside the world."""
        xmove, ymove = random.choice(self.moves)

        new_x = self.pos[0] + xmove
        new_y = self.pos[1] + ymove

        # Keep the peep inside the world boundary.
        if new_x < 0:
            new_x = 0
        if new_y < 0:
            new_y = 0
        if new_x >= xmax:
            new_x = xmax - 1
        if new_y >= ymax:
            new_y = ymax - 1

        self.pos = (new_x, new_y)

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
        return (
            self.name + " @ " + str(self.pos)
            + " happy=" + str(self.happy)
            + " sad=" + str(self.sad)
            + " angry=" + str(self.angry)
        )

    def get_pos(self):
        return self.pos

    def recover_emotions(self):
        """Slowly return emotions to their base values."""

        # Happy returns to base level 50.
        if self.happy < 50:
            self.happy += 1
        if self.happy > 50:
            self.happy -= 1

        # Sad returns to base level 10.
        if self.sad < 10:
            self.sad += 1
        if self.sad > 10:
            self.sad -= 1

        # Angry returns to base level 10.
        if self.angry < 10:
            self.angry += 1
        if self.angry > 10:
            self.angry -= 1

    def step_change(self, world):
        """Move the peep randomly, but do not move into barriers."""
        xmax = world.shape[0]
        ymax = world.shape[1]

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

        # Barrier cells are marked as 11.
        # The peep only moves if the new cell is not a barrier.
        if world[new_x, new_y] != 11:
            self.pos = (new_x, new_y)

        # Update emotional recovery every timestep.
        self.recover_emotions()

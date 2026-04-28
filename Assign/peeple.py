#
# Student Name: <put your name here>
# Student ID  : <put your ID here>
#
# peeple.py - defines the people/actors/creatures in the emotion smulation
#
# Version information:
#    - 2026-03-30 - inital version supplied
# 
# Usage: 
#    <basic information to run program, more complete in README and User Guide
#
import random

def validate_moves(moves, subgrid, blocked_list):
    v_moves = []
    return v_moves

class Peep:
    markers = ['$\U0001F601$', '$\U0001F601$']
    moves = [(0,-1),(1,1)]       # add moves here

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.happy = 0     # Happiness initial value

    def get_pos(self):
        return self.pos

    def step_change(self):
        move = random.choice(self.moves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self, p):
        p.plot(self.pos[0], self.pos[1], marker=self.markers[1])

class Rina:

    pass

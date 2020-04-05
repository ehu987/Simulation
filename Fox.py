import numpy as np
import numpy.linalg as la

class Fox:
    def __init__(self, loc, target):
        self.loc = loc
        self.target = target
        self.state = 0
        self.angle_set = np.pi*np.arange(0, 2, 0.5)
        self.Q = np.ones([1, 4])
        self.action_set = None

    def hunt(self, target):
        self.target = target
    # action functions

    def move(self, new_loc):
        self.loc = new_loc


    # state space functions

    def update_state(self):
        # update the distance from the target, the angle to the target, and the set of possible actions
        self.state = np.array([self.dist(), self.angle()])
        self.action_set = self.enumerate_actions()

    def enumerate_actions(self):
        # find the set of possible actions from the current location relative to the target
        angles = self.angle_set #+ self.state[1]
        return np.array([self.loc[0] + np.cos(angles), self.loc[1] + np.sin(angles)])

    # helper functions
    def dist(self):
        # distance between current location and target
        return la.norm(self.loc - self.target)

    def angle(self):
        # angle between current location and target
        temp = self.target - self.loc
        return np.arctan2(temp[1], temp[0])


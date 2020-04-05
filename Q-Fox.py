import numpy as np
import numpy.linalg as la

class Fox:
    def __init__(self, loc, target, a, g):
        self.Q = np.random.rand(2,2)/5.0 + 1.0
        self.state = 0 #state = 0 means the rabbit is unaware
        self.loc = loc
        self.target = target
        self.a = a
        self.g = g
        self.actions = np.ones([2, 2], dtype=np.float32)
        self.reward = 0
        self.catch = False

    def update_actions(self):
        self.actions[0, :] = np.array([2*np.cos(self.angle()), 2*np.sin(self.angle())])
        self.actions[1, :] = self.actions[0, :]/4

    def select_action(self):
        eps = np.random.rand(1)
        if eps <= 0.05:
            return np.random.binomial(1, 0.5)
        else:
            rewards = self.Q[self.state, :]
            return np.argmax(rewards)

    def iterate_simulation(self):
        # update set of actions given current positions of the fox and the rabbit
        self.update_actions()

        #select an action based on the current Q matrix and take that action
        i_act = self.select_action()
        print(i_act)
        act = self.actions[i_act, :]
        self.move(self.loc + act)
        if self.dist() <= 0.5:
            self.catch = True
            return
        # play out the consequences and rewards of that action
        i_state = self.state
        if i_act == 0:
            self.state = np.random.binomial(1, np.maximum(
                2 - np.exp(self.dist()), np.exp(-1*self.dist())
            ))
        else:
            self.state = np.random.binomial(1, np.exp(-1*self.dist()))

        self.target = self.target + (1 - self.state)*(np.random.rand(2)-0.5)/2 + self.state*self.run_away()
        self.reward = 1/self.dist()
        self.Q[i_state, i_act] = (1 - self.a)*self.Q[i_state, i_act] + self.a*(self.reward + self.g*np.max(self.Q[self.state, :]))

    def one_pass(self):
        self.catch = False
        while self.catch == False:
            self.iterate_simulation()
    def move(self, loc):
        self.loc = loc

    def dist(self):
        return la.norm(self.loc - self.target)

    def run_away(self):
        return np.array([2 *np.cos(self.angle()), 2 *np.sin(self.angle())])

    def angle(self):
        diff = self.target - self.loc
        return np.arctan2(diff[1], diff[0])

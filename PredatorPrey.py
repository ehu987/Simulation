import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib.animation as animation

class Rabbit:
    def __init__(self, v):
        self.v = v  # how fast the rabbit is
        self.fear = 1
        self.alive = True
        self.terror = False

        # state functions

    def born(self):
        self.x = np.random.rand(1)*0.5
        self.y = np.random.rand(1)*0.5

    def move(self):
        if self.terror:
            self.x = self.x + (self.x - self.predator.x)/self.dist(self.predator) * self.v * self.fear
            self.y = self.y + (self.y - self.predator.y)/self.dist(self.predator) * self.v * self.fear
        else:
            theta = 2 * np.pi * np.random.rand(1)
            self.x = self.x + np.cos(theta) * self.v * self.fear
            self.y = self.y + np.sin(theta) * self.v * self.fear

    def aware(self, f):
        self.predator = f
        self.terror = True

    def die(self):
        self.alive = False

    def dist(self, f):
        return np.sqrt((self.x - f.x) ** 2 + (self.y - f.y) ** 2)





class Fox:
    def __init__(self, v):
        self.v = v  # how fast the rabbit is
        self.hunger = 1
        self.alive = True
        self.hunt = False

    # state functions
    def born(self):
        self.x = np.random.rand(1)*5
        self.y = np.random.rand(1)*5

    def target(self, r):
        self.prey = r
        self.hunt = True

    def status(self, t):
        self.hunger = self.hunger * 1.15

    # action functions
    def move(self):
        if self.hunt:
            self.x = self.x - (self.x - self.prey.x)/self.dist(self.prey)*self.v*self.hunger
            self.y = self.y - (self.y - self.prey.y)/self.dist(self.prey)*self.v*self.hunger
        else:
            theta = 2 * np.pi * np.random.rand(1)
            self.x = self.x + np.cos(theta) * self.v * self.hunger
            self.y = self.y + np.sin(theta) * self.v * self.hunger

    def die(self):
        self.alive = False

    # helper functions
    def dist(self, r):
        return np.sqrt((self.x - r.x) ** 2 + (self.y - self.prey.y) ** 2)



def interact(f, r):
    if ((MSE(f, r)) >= 0.2) & ((MSE(f, r)) < 1):
        print('hunt started')
        f.target(r)
    if ((MSE(f, r)) >= 0.2) & ((MSE(f, r)) < 0.5):
        print('prey terrified')
        r.aware(f)
    elif (MSE(f, r)) < 0.2:
        f.die()
        r.die()
        print('hunt completed')


def MSE(f, r):
    return np.sqrt((f.x - r.x)**2 + (f.y - r.y)**2)
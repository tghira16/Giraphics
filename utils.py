import numpy as np
from math import cos, sin
import time
class Timer:
    def __init__(self, text="Elapsed time: {:0.4f} seconds", logger=print):
        self._start_time = None
        self.text = text
        self.logger = logger
    def start(self, label="task"):
        self.label = label
        self.t1 = time.time()
    def stop(self):
        self.t2 = time.time()
        print("Time lapsed for %s: %s" % (self.label, self.t2-self.t1))

def listlike(var):
    if isinstance(var, list):
        return var
    else:
        return [var]


def TopHeavy(self, i, k=4):
    return i ** k


def BottomHeavy(self, i, k=0.25):
    return i ** k


def Linear(self):
    pass


def Taper(self):
    pass


def Bounce(self):
    pass


def colourgradient(self, s):
    return "white"


def norm(x):
    t = 0
    for v in x:
        t += v ** 2
    return t ** (0.5)


# Rotations 3D
def Rx(theta, r=1):
    return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])
    pass


def Rz(theta, r=1):
    return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])


def Ry(theta, r=1):
    return np.array([[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]])

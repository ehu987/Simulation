from q_Fox import Fox
from visualization import animate, animate2
import numpy as np

import matplotlib.pyplot as plt
f = Fox([0,0], [2,2] ,1, 1)
fox_loc, rabbit_loc = f.one_pass()
animate2(fox_loc, rabbit_loc)


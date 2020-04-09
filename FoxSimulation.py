from q_Fox import Fox
from visualization import animate, multi_animate
import numpy as np

import matplotlib.pyplot as plt
f = Fox([0,0], [5,5], 0.75, 0.5)
fox_loc, rabbit_loc = f.multi_pass(10)
multi_animate(fox_loc, rabbit_loc, 'fox chasing rabbit')
print(f.Q)



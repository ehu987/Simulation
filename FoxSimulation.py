import Fox
import numpy as np
import matplotlib.pyplot as plt

f = Fox.Fox(np.array([0, 0]), np.array([1, np.sqrt(3)]))
f.update_state()
print(f.angle_set)
print(f.state[1]*180/np.pi)

fig, ax = plt.subplots(1,1)

ax.plot(f.loc[0], f.loc[1], 'r^')
ax.plot(f.target[0], f.target[1], 'b*')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

x = f.enumerate_actions()
plt.plot(x[0, :], x[1, :], 'ko')
ax.set_aspect('equal', 'box')

ax.plot([f.loc[0], f.target[0]], [f.loc[1], f.target[1]], '-k')


plt.show()
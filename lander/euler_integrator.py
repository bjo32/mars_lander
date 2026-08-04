# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
G = 6.67430e-11
# mass, spring constant, initial position and velocity
m = 1
M = 5.972e24
k = 1
r = np.array([42164000, 0, 0])
v = np.array([0, 3074.6, 0])

# simulation time, timestep and time
t_max = 100000
dt = 10
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
r_list = []
v_list = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    r_list.append(r)
    v_list.append(v)

    # calculate new position and velocity
    if np.linalg.norm(r) == 0:
        a = np.array([0, 0, 0])
    else:
        a = -G * M * r / np.linalg.norm(r)**3
    r = r + dt * v
    v = v + dt * a

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
r_array = np.array(r_list)
v_array = np.array(v_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, r_array, label='r (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()

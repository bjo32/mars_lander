# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 100
dt = 1 #unstable for dt>2, transition occours or 1.8<dt<2
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []

# initialize previous position for Verlet method
x_prev = x - v * dt

# verlet integration
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m
    x_new = 2 * x - x_prev + dt**2 * a
    v = (x_new - x) / dt
    x_prev = x
    x = x_new

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)


# plot the position-time graph
plt.close('all')
plt.figure()
plt.xlabel('time (s)')
plt.ylabel('position / velocity')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()

# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
r = np.array([0, 0, 0])
v = np.array([1, 0, 0])

# simulation time, timestep and time
t_max = 100
dt = 1 #unstable for dt>2, transition occours or 1.8<dt<2
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
r_list = []
v_list = []

# initialize previous position for Verlet method
r_prev = r - v * dt

# verlet integration
for t in t_array:

    # append current state to trajectories
    r_list.append(r)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * r / m
    r_new = 2 * r - r_prev + dt**2 * a
    v = (r_new - r) / dt
    r_prev = r
    r = r_new

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
r_array = np.array(r_list)
v_array = np.array(v_list)


# plot the position-time graph
plt.close('all')
plt.figure()
plt.xlabel('time (s)')
plt.ylabel('position / velocity')
plt.grid()
plt.plot(t_array, r_array, label='r (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()

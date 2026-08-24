# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
G = 6.67430e-11
R_mars = 3.3895e6  # radius of Mars in metres
m = 1
M = 6.42e23
r = np.array([-9e6, 10e6, 0.0])
v = np.array([1000, 1000, 0.0])

# simulation time, timestep and time
t_max = 100000
dt = 1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
r_list = []
v_list = []
altitude_list = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    r_list.append(r)
    v_list.append(v)

    # calculate new position and velocity
    
    eps = R_mars  #if touching mars, set acceleration to zero
    if np.linalg.norm(r) < eps:
        a = np.zeros(3)
        v = np.zeros(3)
    else:
        a = -G * M * r / np.linalg.norm(r)**3
    r = r + dt * v
    v = v + dt * a
    altitude_list.append(np.linalg.norm(r) - R_mars)
    print(r, v, a)

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
r_array = np.array(r_list)
v_array = np.array(v_list)
altitude_array = np.array(altitude_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, r_array, label='r (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.plot(t_array, altitude_array, label='altitude (m)')
plt.legend()


x_vals = r_array[:, 0]
y_vals = r_array[:, 1]

plt.figure()
plt.plot(x_vals, y_vals, label='trajectory')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid(True)
plt.axis('equal')
plt.legend()

plt.show()
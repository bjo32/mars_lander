# Mars orbit plot in the x-y plane, using 3D NumPy vectors for position and velocity.
# This follows the same Verlet structure as spring_by_verlet.py.

import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
MARS_MASS = 6.42e23
MARS_RADIUS = 3.3895e6


def acceleration(r):
    r_norm = np.linalg.norm(r)
    if r_norm == 0:
        return np.array([0.0, 0.0, 0.0])
    return -G * MARS_MASS * r / r_norm**3


def integrate_case(r0, v0, dt=1.0, t_max=20000.0, max_steps=200000):
    r = np.array(r0, dtype=float)
    v = np.array(v0, dtype=float)
    r_prev = r - v * dt

    x_hist = [r[0]]
    y_hist = [r[1]]
    z_hist = [r[2]]

    t = 0.0
    step = 0
    while t <= t_max and step < max_steps:
        # same Verlet pattern as spring_by_verlet.py
        a = acceleration(r)
        r_new = 2 * r - r_prev + dt**2 * a
        v = (r_new - r) / dt
        r_prev = r
        r = r_new

        x_hist.append(r[0])
        y_hist.append(r[1])
        z_hist.append(r[2])

        t += dt
        step += 1

        if np.linalg.norm(r) <= MARS_RADIUS:
            break

    return np.array(x_hist), np.array(y_hist), np.array(z_hist)


# A: direct fall toward Mars
h_drop = 2.0e5
rA = np.array([MARS_RADIUS + h_drop, 0.0, 0.0], dtype=float)
vA = np.array([-2000.0, 0.0, 0.0], dtype=float)

# B: circular orbit around Mars
h_orbit = 2.0e5
R_orbit = MARS_RADIUS + h_orbit
v_circ = np.sqrt(G * MARS_MASS / R_orbit)
rB = np.array([R_orbit, 0.0, 0.0], dtype=float)
vB = np.array([0.0, v_circ, 0.0], dtype=float)

# C: parabolic orbit around Mars (escape speed, threshold case)
R_parab = MARS_RADIUS + 2.0e5
v_esc = np.sqrt(2.0 * G * MARS_MASS / R_parab)
rC = np.array([R_parab, 0.0, 0.0], dtype=float)
vC = np.array([0.0, v_esc, 0.0], dtype=float)

xA, yA, zA = integrate_case(rA, vA)
xB, yB, zB = integrate_case(rB, vB)
xC, yC, zC = integrate_case(rC, vC)

# Mars surface for reference in the x-y plane
theta = np.linspace(0, 2 * np.pi, 400)
planet_x = MARS_RADIUS * np.cos(theta)
planet_y = MARS_RADIUS * np.sin(theta)

fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(xA, yA, label='A: direct fall', color='tab:blue')
ax.plot(xB, yB, label='B: circular orbit', color='tab:orange')
ax.plot(xC, yC, label='C: parabolic orbit', color='tab:green')
ax.plot(planet_x, planet_y, 'k--', linewidth=1.5, label='Mars surface')
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('Mars trajectories in the x-y plane')
ax.grid(True, alpha=0.3)
ax.legend()
plt.tight_layout()
plt.show()

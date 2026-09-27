from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

data_path = Path(__file__).resolve().parent / "trajectories.txt"
if not data_path.exists():
    raise FileNotFoundError(f"Trajectory file not found: {data_path}")

results = np.loadtxt(data_path)

plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(results[:, 0], results[:, 1], label='x (m)')
plt.plot(results[:, 0], results[:, 2], label='v (m/s)')
plt.legend()
plt.show()
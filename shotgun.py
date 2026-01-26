import numpy as np
import matplotlib.pyplot as plt
from single_particle import update_particle

DT = 0.05
G_ACCEL = np.array([0, -9.81])

def main():
    rng = np.random.default_rng()

    pos = np.zeros((100,2))
    vel = np.zeros((100,2))
    thetas = 45 + 12*rng.standard_normal(100)
    v0 = 50 + 5*rng.standard_normal(100)
    vel[:, 0] = v0*np.cos(np.radians(thetas))
    vel[:,1] = v0*np.sin(np.radians(thetas))

    history = [pos.copy()]
    while any(vel[:, 0] > 0):
        mask = np.linalg.norm(vel, axis =1) > 0
        pos[mask], vel[mask] = update_particle(pos[mask], vel[mask], 0.1, 1)
        landed = mask & (pos[:, 1] < 0)
        pos[landed,1] = 0
        vel[landed] = 0
        history.append(pos.copy())
    history = np.array(history)
    plt.figure(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, 100)) 
    for i in range(100):
        x_vals = history[:, i, 0]
        y_vals = history[:, i, 1]
        plt.plot(x_vals, y_vals, color=colors[i], alpha=0.6)
    plt.axhline(0, color='black', lw=2) 
    plt.show()
if __name__ == "__main__":
    main()
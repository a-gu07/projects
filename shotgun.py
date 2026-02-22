import numpy as np
import matplotlib.pyplot as plt
from single_particle import update_particle
"""
A kinematics simulator to model the launch of 100 particles at once from the same initial position(like a shotgun!).
Launch angles and initial velocities are distributed around 45 and 50, respectively. Standard SI units are used.
"""

DT = 0.01
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
    while any(np.linalg.norm(vel, axis =1) > 0):
        mask = np.linalg.norm(vel, axis =1) > 0
        pos[mask], vel[mask] = update_particle(pos[mask], vel[mask], 0.1, 1, DT, G_ACCEL)
        landed = mask & (pos[:, 1] < 0)
        pos[landed,1] = 0
        vel[landed] = 0
        history.append(pos.copy())
    history = np.array(history)
    plt.figure(figsize=(10, 5))
    colors = plt.cm.viridis(np.linspace(0, 1, 100)) 
    for i in range(100):
        x_vals = history[:, i, 0]
        y_vals = history[:, i, 1]
        plt.plot(x_vals, y_vals, color=colors[i], alpha=0.5)
    plt.grid(True)
    plt.title("100 Particles!")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.axhline(0, color='black', lw=2) 
    plt.show()

if __name__ == "__main__":
    main()
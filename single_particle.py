import numpy as np
import matplotlib.pyplot as plt

DT = 0.01
G_ACCEL = np.array([0, -9.81])
""" A program to model projectile motion of a single particle. Uses g = -9.81 and F_drag = -kv^2. Each time step is 0.01 s"""

def update_particle(pos, vel, drag_coeff, mass, dt, g_accel):
    speed = np.linalg.norm(vel, axis=(vel.ndim -1), keepdims = True)
    drag = -drag_coeff*speed*vel
    accel =  g_accel + drag/mass
    v_new = vel + accel*dt
    p_new = pos + v_new*dt
    return p_new, v_new

def get_input():
    try:
        k = float(input("Drag coefficient: ") or 0.1)
        m = float(input("Mass: ") or 1.0)
        theta = float(input("Launch angle(degrees): ") or 45)
        v0 = float(input("Initial speed: ") or 10)
        if any (a<0 for a in [k,m,v0]) or not (0<=theta<=90):
            print("Error: Values must be positive and angle between 0-90.")
            exit()
    except ValueError:
        print("Invalid input. ")
        exit()
    return k,m,theta, v0

def main():
    k, m, theta_deg, v0 = get_input()
    theta_rad = np.radians(theta_deg)
    pos = np.array([0,0])
    vel = np.array([np.cos(theta_rad), np.sin(theta_rad)])*v0

    x_path = [pos[0]]
    y_path = [pos[1]]
    while(len(y_path) == 1 or pos[1]>=0):
        pos,vel = update_particle(pos, vel, k, m, DT, G_ACCEL)
        x_path.append(pos[0])
        y_path.append(pos[1])
        first = False

    plt.figure(figsize=(10, 5))
    plt.plot(x_path, y_path, label=f"Angle: {theta_deg}°, k={k}")
    plt.axhline(0, color='black', lw=2)
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.title("Projectile Path with Air Drag")
    plt.legend()
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    main()
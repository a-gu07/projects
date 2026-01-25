import numpy as np
import matplotlib.pyplot as plt


""" A program to model projectile motion of a single particle. Uses g = -9.81 and F_drag = -kv^2. Each time step is 0.01 s"""

try:
    k = float(input("Drag coefficient: ") or 0.1)
    m = float(input("Mass: ") or 1.0)
    theta = float(input("Launch angle(degrees): ") or 45)
    v0 = float(input("Initial speed: ") or 10)
    if any( a<0 for a in [k,m,v0] or not (0<=theta<=90)):
        print("Error: Values must be positive and angle between 0-90.")
        exit()
except ValueError or (k or m or theta or s_initial)<0:
    print("Invalid input. ")
    exit()

dt = 0.01
g = np.array([0, -9.81])
theta = np.radians(theta)
pos = np.array([0,0])
vel = np.array([np.cos(theta), np.sin(theta)])*v0

def update(p, v):
    speed = np.linalg.norm(v)
    drag = -v*k*speed
    a =  g + drag/m
    v_new = v + a*dt
    p_new = p + v_new*dt
    return p_new, v_new

count = 0
x = [pos[0]]
y = [pos[1]]
while(count == 0 or pos[1]>=0):
    pos,vel = update(pos, vel)
    x.append(pos[0])
    y.append(pos[1])
    count+=1

plt.figure(figsize=(10, 5))
plt.plot(x, y, label=f"Angle: {np.degrees(theta)}°, k={k}")
plt.axhline(0, color='black', lw=2) # The ground
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Path with Air Drag")
plt.legend()
plt.grid(True)
plt.show()
    

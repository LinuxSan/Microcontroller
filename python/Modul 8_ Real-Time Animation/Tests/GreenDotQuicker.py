import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Opret figur og akse
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # X-akse område
ax.set_ylim(0, 10)  # Y-akse område

# Opret lister til data
Redxdata, Redydata = [], []
Greenxdata, Greenydata = [], []


# Opret en rød prik, der skal animeres
ln, = ax.plot([], [], 'ro')
gn, = ax.plot([], [], 'go')

def init():
    ln.set_data([], [])
    gn.set_data([], [])
    return ln, gn,

def update(frame):
    if frame % 2 == 0:  # Opdater rød data kun for hver anden frame
        Redxdata.append(frame)  # Tilføj ny x-værdi
        Redydata.append(np.random.uniform(0, 10))  # Tilføj ny y-værdi
        ln.set_data(Redxdata, Redydata)  # Opdater plottet
    Greenxdata.append(frame)  # Tilføj ny x-værdi
    Greenydata.append(np.random.uniform(0, 10))  # Tilføj ny y-værdi
    gn.set_data(Greenxdata, Greenydata)  # Opdater plottet
    return ln, gn,

# Opret animation
#Ædring af inteval ændre hvor hyppigt animationen bliver opdateret
ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=20, blit=True)

# Vis animation
plt.show()
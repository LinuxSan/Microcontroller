import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Opret figur og akse
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # X-akse område
ax.set_ylim(0, 10)  # Y-akse område

# Opret lister til data
xdata, ydata = [], []

# Opret en rød prik, der skal animeres
ln, = ax.plot([], [], 'ro')

def init():
    ln.set_data([], [])
    return ln,

def update(frame):
    xdata.append(frame)  # Tilføj ny x-værdi
    ydata.append(np.random.uniform(0, 10))  # Tilføj ny y-værdi
    ln.set_data(xdata, ydata)  # Opdater plottet
    return ln,

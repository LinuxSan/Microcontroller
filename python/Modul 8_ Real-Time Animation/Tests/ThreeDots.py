import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Opret figur og akse
fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Opret to prikker: rød og blå
ln1, = ax.plot([], [], 'ro', label="Prik 1")
ln2, = ax.plot([], [], 'bo', label="Prik 2")
gn1, = ax.plot([], [], 'go', label="Prik 3")

xdata, y1data, y2data, y3data = [], [], [], []

def init():
    ln1.set_data([], [])
    ln2.set_data([], [])
    gn1.set_data([], [])
    return ln1, ln2, gn1

def update(frame):
    """
    Updates the data for the animation on each frame.

    Parameters:
    frame (int): The current frame number in the animation.

    Functionality:
    - On even frames:
        - Appends the scaled frame number (frame // 2) to the x-axis data for red and blue dots.
        - Appends a random y-coordinate (between 0 and 10) to the y-axis data for red and blue dots.
        - Updates the red and blue dot line objects (`ln1` and `ln2`) with the new data.
    - On every frame:
        - Appends a random y-coordinate (between 0 and 10) to the y-axis data for the green dot.
        - Updates the green dot line object (`gn1`) with the new data.

    Returns:
    tuple: Updated line objects (`ln1`, `ln2`, `gn1`) for red, blue, and green dots, respectively.
    """
    if frame % 2 == 0:  # Update red and blue dots on even frames
        xdata.append(frame // 2)  # Scale x-axis for red and blue dots
        y1data.append(np.random.uniform(0, 10))
        y2data.append(np.random.uniform(0, 10))
        ln1.set_data(xdata, y1data)
        ln2.set_data(xdata, y2data)
    # Update green dot on every frame
    y3data.append(np.random.uniform(0, 10))
    gn1.set_data(range(len(y3data)), y3data)
    return ln1, ln2, gn1

# Opret animation
ani = FuncAnimation(fig, update, frames=range(20), init_func=init, interval=500, blit=True)

# Vis legend og animation
plt.legend()
plt.show()
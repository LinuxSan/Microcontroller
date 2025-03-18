import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Opret figur med to subplots (1 række, 3 kolonner)
fig, (ax1, ax2, ax3,) = plt.subplots(1, 3, figsize=(10, 5))

# Indstil aksegrænser
ax1.set_xlim(0, 10)
ax1.set_ylim(20, 30)
ax1.set_title("Temperatur")

ax2.set_xlim(0, 10)
ax2.set_ylim(40, 60)
ax2.set_title("Fugtighed")

ax3.set_xlim(0, 10)
ax3.set_ylim(70, 90)
ax3.set_title("Lufttryk")

# Opret linjer for temperatur og fugtighed i hvert subplot
ln1, = ax1.plot([], [], 'ro', label="Temperatur")
ln2, = ax2.plot([], [], 'bo', label="Fugtighed")
ln3, = ax3.plot([], [], 'go', label="Lufttryk")

xdata, temp_data, hum_data, Luft_data = [], [], [], []

def init():
    ln1.set_data([], [])
    ln2.set_data([], [])
    ln3.set_data([], [])
    return ln1, ln2, ln3,

def update(frame):
    xdata.append(frame)
    temp_data.append(22 + np.random.normal(0, 0.5))  # Simuleret temperatur
    hum_data.append(50 + np.random.normal(0, 2))  # Simuleret fugtighed
    Luft_data.append(70 + np.random.normal(0, 5))

    ln1.set_data(xdata, temp_data)
    ln2.set_data(xdata, hum_data)
    ln3.set_data(xdata, Luft_data)
    return ln1, ln2, ln3,

# Opret animation
ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=500, blit=False)

ax1.legend()
ax2.legend()
ax3.legend()
plt.tight_layout()
plt.show()
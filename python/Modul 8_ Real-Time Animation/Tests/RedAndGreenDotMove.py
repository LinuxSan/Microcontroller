import numpy as np  # Import the NumPy library for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from matplotlib.animation import FuncAnimation  # Import FuncAnimation for creating animations

# Create figure and axis
fig, ax = plt.subplots()  # Create a figure and a set of subplots (axes)
ax.set_xlim(0, 10)  # Set the range of the X-axis from 0 to 10
ax.set_ylim(0, 10)  # Set the range of the Y-axis from 0 to 10

# List to hold data for multiple dots
dots = [  # Define a list of dictionaries, each representing a dot with its properties
    {"color": "red", "xdata": [], "ydata": [], "plot": None},  # Red dot with empty data
    {"color": "green", "xdata": [], "ydata": [], "plot": None},  # Green dot with empty data
    # Add more dots here with different colors if needed
]

# Initialize plots for each dot
for dot in dots:  # Loop through each dot in the list
    dot["plot"], = ax.plot([], [], marker="o", color=dot["color"], linestyle="")  
    # Create a plot for each dot with its specified color and marker style

def init():
    # Initialization function to reset the data for all dots
    for dot in dots:  # Loop through each dot
        dot["plot"].set_data([], [])  # Reset the data for the plot
    return [dot["plot"] for dot in dots]  # Return the list of plot objects

def update(frame):
    # Update function to modify the data for each frame of the animation
    for dot in dots:  # Loop through each dot
        dot["xdata"].append(frame)  # Append the current frame number to the X data
        dot["ydata"].append(np.random.uniform(0, 10))  # Append a random Y value between 0 and 10
        dot["plot"].set_data(dot["xdata"], dot["ydata"])  # Update the plot with new data
        print(dot, "\n\n\n\n")  # Debug: Print the current dot's data
        print(dots, "\n\n\n\n")  # Debug: Print the entire dots list
    return [dot["plot"] for dot in dots]  # Return the updated list of plot objects

# Create animation
ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=200, blit=True)
# Create an animation object that updates the plot every 200ms for 10 frames

# Show animation
plt.show()  # Display the animation

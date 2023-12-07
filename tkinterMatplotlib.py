import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap

# Initial data
categories = ['Brakes']
values = [1]

# Create a Tkinter app
root = tk.Tk()
root.title('Matplotlib Tkinter App')

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()
bar = ax.bar(categories, values, color='skyblue')
ax.set_xlabel('Sources')
ax.set_ylabel('Temperature (Celsius)')
ax.set_title('Temperature Analysis')

# Set the maximum y-value
max_y_value = 110
ax.set_ylim(0, max_y_value)

# Create a Matplotlib canvas for embedding in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a colormap for gradient effect
cmap = LinearSegmentedColormap.from_list('custom_gradient', ['blue', 'skyblue', 'lightblue', 'white', 'yellow', 'orange', 'red', 'darkred'])

# Function to update the bar graph
def update(frame):
    if (values[0] >= 100):
        values[0] = 1
    values[0] *= 1.05  # Increase the value by 10%
    for bar_, h in zip(bar, values):
        normalized_height = h / max_y_value
        bar_.set_height(h)
        bar_.set_color(cmap(normalized_height))

# Create an animation
ani = FuncAnimation(fig, update, frames=None, interval=100, cache_frame_data=False)

# Start the Tkinter event loop
root.mainloop()

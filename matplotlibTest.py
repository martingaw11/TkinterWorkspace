import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap

# Initial data
categories = ['Brakes']
values = [1]

# Create a bar graph
fig, ax = plt.subplots()
bar = ax.bar(categories, values, color='skyblue')

# Set the maximum y-value
max_y_value = 100
ax.set_ylim(0, max_y_value)

# Create a colormap for gradient effect
cmap = LinearSegmentedColormap.from_list('custom_gradient', ['blue', 'skyblue', 'lightblue', 'white', 'yellow', 'orange', 'red', 'darkred'])

# Function to update the bar graph
def update(frame):
    values[0] *= 1.1  # Increase the value by 10%
    
    # Set the color based on a gradient
    for bar_, h in zip(bar, values):
        normalized_height = h / max_y_value
        bar_.set_height(h)
        bar_.set_color(cmap(normalized_height))

# Create an animation
ani = FuncAnimation(fig, update, frames=range(10), interval=100)

# Show the plot
plt.show()

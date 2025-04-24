
import matplotlib.pyplot as plt
import numpy as np

# Set dark mode background color
plt.style.use('dark_background')

# Generate random data points
num_points = 789
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Create the scatter plot
plt.scatter(x, y, c=x, 
  cmap='Greens', #'plasma', 
  edgecolors='black')  # Adjust marker size as needed

# Set plot labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Random Data (Plasma Colormap)')

# Display the plot
plt.show()

# Import libraries
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Heatmap() function for generating heatmaps
def Heatmaps():
    # Read the CSV file
    df = pd.read_csv('coordinates_dates_2022.csv')

    # Process the data to get a frequency map of coordinates
    coordinate_counts = df.groupby(['coordinate1_lat', 'coordinate1_lon']).size()

    # Create a higher resolution 2D grid for the heatmap
    grid_size = 100  
    heatmap_grid = np.zeros((grid_size, grid_size))

    # Fill the grid with frequency data
    for (lat, lon), count in coordinate_counts.items():
        x = int((lat + 90) / 180 * (grid_size - 1))
        y = int((lon + 180) / 360 * (grid_size - 1))
        x = max(0, min(x, grid_size - 1))
        y = max(0, min(y, grid_size - 1))
        heatmap_grid[x, y] = count

    # Normalize the grid for image intensity
    heatmap_grid_normalized = heatmap_grid / heatmap_grid.max()

    # Apply a colormap (using Matplotlib colormaps)
    cmap = plt.cm.viridis 
    colored_heatmap = cmap(heatmap_grid_normalized)

    # Convert to image, rotate, and resize
    img = Image.fromarray((colored_heatmap[:, :, :3] * 255).astype(np.uint8))
    img = img.rotate(90) # Rotate
    img = img.resize((1000, 1000))  # Resize 

    # Save and show the image
    img.save('heatmap.png')
    img.show()

# Function call
Heatmaps()

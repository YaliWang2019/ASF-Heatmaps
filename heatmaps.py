# Import libraries
import pandas as pd
from PIL import Image
import numpy as np

# Heatmap function for generating heatmaps
def Heatmaps():
    # Read CSV file
    df = pd.read_csv('coordinates_dates_100000.csv')

    # Process data to get a frequency map of coordinates
    coordinate_counts = df.groupby(['coordinate1_lat', 'coordinate1_lon']).size()

    # 2D grid for the heatmap
    grid_size = 100
    heatmap_grid = np.zeros((grid_size, grid_size))

    # Fill grid with frequency data
    for (lat, lon), count in coordinate_counts.items():
        x = int((lat + 90) / 180 * (grid_size - 1))  # Convert latitude to a grid coordinate
        y = int((lon + 180) / 360 * (grid_size - 1))  # Convert longitude to a grid coordinate

        # Ensure x and y are within the bounds of the grid
        x = max(0, min(x, grid_size - 1))
        y = max(0, min(y, grid_size - 1))

        heatmap_grid[x, y] = count

    # Normalize the grid for image intensity
    heatmap_grid = (255 * heatmap_grid / heatmap_grid.max()).astype(np.uint8)

    # Create and save the heatmap image
    img = Image.fromarray(heatmap_grid, 'L')
    img = img.resize((1000, 500))  # Resize 
    img.show()

# Function call(s)
Heatmaps()
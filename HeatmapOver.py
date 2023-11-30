# Import libraries
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import geopandas as gpd

# Function to plot world map outline
def plot_world_map(ax):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.plot(ax=ax, color='none', edgecolor='black', linewidth=1)

# Heatmap() function for generating heatmaps
def Heatmaps():
    # Read the larger CSV file with 800,000 data points
    df = pd.read_csv('coordinates_dates_2022.csv')  # Make sure to replace with your actual file name

    # Process the data to get a frequency map of coordinates
    coordinate_counts = df.groupby(['coordinate1_lat', 'coordinate1_lon']).size()

    # Create a higher resolution 2D grid for the heatmap
    grid_size = 200  # Increase grid size for more data points
    heatmap_grid = np.zeros((grid_size, grid_size))

    # Fill the grid with frequency data
    for (lat, lon), count in coordinate_counts.items():
        # Adjust rounding logic for coordinates along the border
        x = int((lat + 90) / 180 * (grid_size - 1))
        y = int((lon + 180) / 360 * (grid_size - 1))
        x = max(0, min(x, grid_size - 1))
        y = max(0, min(y, grid_size - 1))
        heatmap_grid[x, y] = count

    # Normalize the grid for image intensity
    heatmap_grid_normalized = heatmap_grid / heatmap_grid.max()

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot the heatmap
    cmap = plt.cm.viridis 
    colored_heatmap = cmap(heatmap_grid_normalized)
    img = ax.imshow(colored_heatmap, extent=[-180, 180, -90, 90])

    # Convert to image, rotate, and resize
    img = Image.fromarray((colored_heatmap[:, :, :3] * 255).astype(np.uint8))
    img = img.rotate(90) # Rotate
    img = img.resize((1000, 1000))  # Resize 

    # Overlay world map outline
    plot_world_map(ax)

    # Save and show the image
    plt.savefig('heatmap_with_world_map.png')
    plt.show()

# Function call
Heatmaps()

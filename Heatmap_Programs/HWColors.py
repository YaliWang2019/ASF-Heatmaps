# Import libraries
import pandas as pd
import numpy as np
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import geopandas as gpd #geopandas for the world overlay

# Function to plot world map outline
def plot_world_map(ax):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.plot(ax=ax, color='none', edgecolor='black', linewidth=1)

# Heatmap() function for generating custom-colored heatmaps
def Heatmaps():
    # Read the larger CSV file with 800,000 data points
    df = pd.read_csv('coordinates_dates_2022.csv')  

    # Process the data to get a frequency map of coordinates
    coordinate_counts = df.groupby(['coordinate1_lat', 'coordinate1_lon']).size()

    # Create a higher resolution 2D grid for the heatmap
    grid_size = 150  # Increase grid size for more data points
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

    # Rotate the data using NumPy
    rotated_heatmap = np.rot90(heatmap_grid_normalized)

    # Define custom colors based on the number of data points
    colors = ['#ffffcc', '#ffeda0', '#fed976', '#feb24c', '#fd8d3c', '#fc4e2a', '#e31a1c', '#bd0026', '#800026']

    # Create a custom colormap
    custom_cmap = ListedColormap(colors)

    # Determine the extent based on the data range
    min_lat, max_lat = df['coordinate1_lat'].min(), df['coordinate1_lat'].max()
    min_lon, max_lon = 1.8*df['coordinate1_lon'].min(), 1.8*df['coordinate1_lon'].max()

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))

    # Overlay world map outline
    plot_world_map(ax)

    # Plot the heatmap with custom colors
    img = ax.imshow(rotated_heatmap, cmap=custom_cmap, extent=[min_lat, max_lat, min_lon, max_lon])

    # Save and show the image
    plt.savefig('heatmap_OverMap.png')
    #plt.show()

# Function call
Heatmaps()

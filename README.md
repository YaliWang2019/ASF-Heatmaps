# ASF-Heatmaps
## 1 Introduction
	
### 1.1 Overview
The ASF Heatmaps Program is engineered to generate a two-dimensional heatmap displaying the geophysical footprint while determining the coverage density through the optimized use of Sentinel-1 data in the ASF archive. The geophysical footprint refers to the product of what is generated through the geometric coordinates and specific properties gathered during orbit from the satellite-retrieved Sentinel-1 data. Each record of these geographical footprints is a polygonal area formed by 5 coordinates. Through these polygon geophysical footprints, coverage density is interpreted into a visual representation as a heatmap. The project is aimed to be completed by a student team from the University of Alaska Fairbanks within 5 weeks.
	
### 1.2 Motivation
Using various APIs to pull databases from the Common Metadata Repository (CMR) is time-consuming, especially when people need to visually get a coverage overview of certain regions from these databases. Our motivation for advancing this project is to build a simple but convenient graphic user interface (GUI) tool that allows users to get heat maps by sending queries to intuitively browse the entire world map or coverage information of a specific region. Our project is to provide scientists or researchers with easy-to-use tools for generating data coverage heat maps. This project uses data whose beam mode is IW in 2022. If the user needs to use the data from other years or beam modes, the user only needs to replace the database to get the required heat maps.

### 1.3 Technology Used
The data set is stored in Pandas DataFrame and GeoPandas DataFrame from the CSV file. All the data queries are done within the DataFrame objects. The technology used to engineer the ASF Heatmaps Program primarily includes the Python programming language utilizing its powerful libraries for data interpretation: Pandas, GeoPandas, NumPy, Matplotlib, and Shapely. In addition, the Tkinter GUI library was also used to create an interactive graphical user interface, allowing the user to request custom options.

Pandas and GeoPandas libraries mainly store datasets in the form of DataFrame. The NumPy library processes vertically flipped data columns to make correct heatmaps using Matplotlib. We decided to use the Shapely library for geometric operations and shapes in geospatial applications rather than using PIL (Python Imaging Library). On the one hand, we are using the polygon property of the data set, which can be properly handled with shapely. geometry. On the other hand, we are counting the intersects of the polygons, which can be better implemented using shapely.geometry since it provides a higher-level abstraction for geometries, making it easier to work with complex shapes and perform spatial operations. Still, we kept the Pillow library for potential future implementations and improvements of this project. 

## 2 Requirements and Instructions

### 2.1 Requirements
Necessary requirements for the ASF Heatmaps program include having either a Python or Conda environment set up on your system. Then, you will need to make sure to have the following Python libraries installed on your environment: pandas, geopandas, shapely, numpy, Pillow, matplotlib, tk, fsspec, requests, and aiohttp. The requests and aiohttp libraries are required to install when running the script on Chinook HPC. If you do not currently have these installed in your desired environment, you can do so by executing the following commands in your terminal:
```
pip install -r Requirements.txt
```
### 2.2 Instructions
In this project, the horizontal and vertical divisions of the spatial area of the generated heat map are both 150. Two CSV data sets are required to generate the heat map, coordinates_dates_2022.csv, and polygon_only_2022.csv, both of which are included in this repository. coordinates_dates_2022.csv contains records with beam mode IW for the whole year of 2022. Each record contains the longitude and latitude of five coordinates and the query time. The information contained in polygon_only_2022.csv is: after horizontally and vertically dividing the polygon formed by the five coordinates of each record of coordinates_dates_2022.csv, the number of intersecting polygons, and the query time.

Once you have installed all the required libraries necessary to run the ASF Heatmaps Application, you can do so by running the Python script HM_Integrated.py through the following command, where you will be brought to the ASF Heatmaps Program’s user interface:
```
python HM_Integrated.py
```
In the user interface, you will be prompted to select an option from the following: Display a Country on World Map, Generate Custom Heatmap Using Dates, Generate Custom Heatmap Using Dates and Coordinates, Full World Heatmap, or Exit. 

The choice of Display a Country on World Map prompts you to input the Country name, for example, United States of America. Then, the window will continue to prompt you to input the start date and end date of your query, both in YYYY-MM-DD format. After the user inputs these values, the program will use them to generate the required heat map. The heat map generation will take approximately half a minute to several minutes, depending on the machine's performance you are working on.

Generate Custom Heatmap Using Dates button prompts you to input the start date and end date of your query, both in YYYY-MM-DD format. After the user inputs these values, the program will use them to generate the required heat map. The heat map generation will take approximately half a minute to several minutes, depending on the machine's performance you are working on.

Generate Custom Heatmap Using Dates and Coordinates prompts you to input the start date and end date of your query, both in YYYY-MM-DD format. After taking the dates inputs, the window will prompt you to enter four coordinates: minimum latitude, maximum latitude, minimum longitude, and maximum longitude, which all can be integers or floats. After the user inputs these values, the program will use them to generate the required heat map. The heat map generation will take approximately half a minute to several minutes, depending on the machine's performance you are working on.

Full World Heatmap produces a heatmap of the entire world. This button does not prompt you to enter any value; it uses the polygon_only_2022.csv to generate the heat map directly without going through the division work of the spatial area. Thus, it should be the fastest process, only taking seconds to generate the full-year heat map. 
The Exit option simply terminates the ASF Heatmap Program.

## 3 Future Implementations
	
### 3.1 Display Oceans and Lands on the Base World Map
According to the example pattern provided by the stakeholder, continents and oceans have different colors in the world map below the heat map. Ultimately, our product did not implement this function; the continents and oceans don't have colors. Theoretically, this could be achieved using map data from the Natural Earth Data website. Due to the time constraints of this semester, we only explored a little. But in future work, we hope to be able to achieve this.

### 3.2 Optimization of User Interface
Our ideal design was: for each option to create a heat map, after creating the heat map, the UI window can return to the original menu interface. So far, only after generating the full-year heatmap can the UI window return to the menu interface for the user to make other choices. For other options for generating heat maps, the UI window is closed immediately after creating the heat map, while the program does not exit and is still running. Our next goal is to realize that no matter what kind of heat map is created, the UI window can return to the original menu interface so that the user can choose to create other heat maps or actively click Exit to exit the program.

### 3.3 Check and Adjust the Generated Heatmap Overlay Position
Although the generated heat maps do not appear to have a very obvious shift overall, we are concerned that the heat maps actually have a slight shift that is not visible to the naked eye. In addition, occasionally, some dark color patches extend into the ocean areas near the continent, which is also strange. We will check the precise location of the generated heat map overlap on the map and make some adjustments in later work.

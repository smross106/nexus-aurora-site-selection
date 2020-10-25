# import necessary packages
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et


#Location of file. Obviously change this for your system
rel_path = 'OneDrive/Documents/Nexus Aurora/Site selection/nexus-aurora-site-selection/shapetest.shp'

path = os.path.join(os.getcwd(),rel_path)

#Import the 
rivers = gpd.read_file(path)

#Print out the rivers just as a check
print(rivers.cx[:,:0])


#Create a new data field of "points" which has all the coordinates of each river in a list of doubles
rivers['points'] = rivers.apply(lambda x: [y for y in x['geometry'].coords], axis=1)


#Print out some of these to test
print(valleys['points'][0:2])
print(int(valleys["VNOrder"][1]))


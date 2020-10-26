# import necessary packages
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et
import numpy as np

"""
TODO

Put everything into functions

"""


#Location of file. Obviously change this for your system
rel_path = 'OneDrive/Documents/Nexus Aurora/Site selection/nexus-aurora-site-selection/shapetest.shp'

path = os.path.join(os.getcwd(),rel_path)

#Import the 
rivers = gpd.read_file(path)

#Print out the rivers just as a check
print(rivers.cx[:,:0])


#Create a new data field of "points" which has all the coordinates of each river in a list of doubles
rivers['points'] = rivers.apply(lambda x: [y for y in x['geometry'].coords], axis=1)


#Extract the data required
pointLists =  list(rivers['points'])
orderLists = list(rivers['VNOrder'])


lat_range = np.zeros(180)
lat_values = list(range(-90,90))
lon_range = np.zeros(360)
lon_values = list(range(-180,180))

all_range = np.zeros((180,360))

for i in range(len(pointLists)):
    order = orderLists[i]
    for k in pointLists[i]:
        lat = int(k[1])+90
        lon = int(k[0])
        lat_range[lat]+=order
        lon_range[lon]+=order
        all_range[lat][lon]+=order



#p1 = plt.bar(lon_values, lon_range)
plt.contourf(all_range)
plt.colorbar()
plt.show()

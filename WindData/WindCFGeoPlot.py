#Geo plot of CF for wind energy
import numpy as np
import pandas as pd
import geoplot as gplt
import geopandas as gpd
import matplotlib.colors as clrs
import matplotlib.pyplot as plt


ShapeFileCoast="./GEOData/ne_10m_coastline.shp"
ShapeFileStates="./GEOData/ne_10m_admin_1_states_provinces_lines.shp"

HourData=np.load('WindEnergyNREL_100m_ERGIS.npz')#Energy Data

HourWindEnergy=HourData["WindEnergy"]

AvgWindEnergy=np.average(HourWindEnergy,axis=1)

LatLong=HourData["LatLong"]


min_longitude=-78.7
max_longitude=-74.5

min_latitude=33.7
max_latitude=36.7

xlim =[min_longitude,max_longitude]
ylim=[min_latitude, max_latitude]

df = gpd.read_file(ShapeFileCoast)
df1 = gpd.read_file(ShapeFileStates)

fig, ax = plt.subplots(figsize  = None)

df.plot(color='black',linewidth=1,ax=ax)
df1.plot(color='black',linewidth=1,ax=ax)

plt.scatter(LatLong[:,1],LatLong[:,0],c=AvgWindEnergy, s=0.2, cmap='jet')

clb = plt.colorbar()
clb.ax.set_title('CF')

ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.title("Wind Energy Sites")

plt.savefig('CF_WindNC_2007_2014.png',dpi=700)


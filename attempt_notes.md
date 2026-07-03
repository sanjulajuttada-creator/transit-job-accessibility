## Approach considered
using r5py
1. build a transport network by loading the GTFS feed & OpenStreetMap street network for dallas area
2. set the origin points (centroid) of each Dallas census tract - find it from the shapefile
3. using r5py.Isochrones
- i can run the isochrone computation. pass the network, the orignis, departure times, transport modes(transit + walk), and the cutoff times (15, 30, 45, 60) minutes
4. with each resulting isochrone, spatially join it against the LODES job counts 
- the METRANS paper did a 'cookie-cutter' overlay logic to count the reachable jobs per tract

## What I tried
1 and 2 downloaded
3. try to crop the osm file down to just the dfw area
4. since fares are irrelevant to traveltime/isochrone analysis

## Barriers encountered
1. r5py's engine requires Java 21 installed seperately
2. r5py also needs a seperate OpenStreetMap extract for the DFW area
3. first attempt used the full texas OSM extract but r5py said it was too big
4. r5py rejected DART's fare_attributes.txt
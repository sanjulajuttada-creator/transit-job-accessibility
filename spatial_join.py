import geopandas as gpd
import pandas as pd

# cesus tract shapes
print("Loading census tracts...")
tracts = gpd.read_file("shapefiles/tl_2025_48_tract.shp")

# FIPS like code strings
tracts["GEOID"] = tracts["GEOID"].astype(str)

# filter to Dallas County (county FIPS 113)
dallas = tracts[tracts["COUNTYFP"] == "113"].copy()
print(f"Dallas County tracts: {len(dallas)}")

# checking w coordinate system
print(f"CRS: {dallas.crs}")

# load/clean the income data
print("\nLoading income data...")
income = pd.read_csv("census/income_2023.csv", skiprows=[1])  

# extracting the GEOID 
income["GEOID"] = income["GEO_ID"].str.split("US").str[1]

income = income[["GEOID", "B19013_001E"]].copy()
income = income.rename(columns={"B19013_001E": "median_income"})

# converting the income to a number 
income["median_income"] = pd.to_numeric(income["median_income"], errors="coerce")

print(f"Cleaned income shape: {income.shape}")
print(income.head(3))

# tabular join
print("\nJoining income to tracts...")
dallas = dallas.merge(income, on="GEOID")
print(f"Tracts with income attached: {len(dallas)}")
print(dallas[["GEOID", "median_income"]].head(3))

# load the dart data stops as geographic points
print("\nLoading DART stops...")
stops = pd.read_csv("gtfs/stops.txt")
print(f"Total DART stops: {len(stops)}")

# convert the stops (w lat/lon columns) into geographic points
stops_gdf = gpd.GeoDataFrame(
    stops,
    geometry=gpd.points_from_xy(stops["stop_lon"], stops["stop_lat"]),
    crs="EPSG:4269"  # match the tracts' coordinate system
)
print(f"CRS of stops: {stops_gdf.crs}")

# spatial join
print("\nPerforming spatial join...")
stops_with_tract = stops_gdf.sjoin(dallas, predicate="within")
print(f"Stops matched to a Dallas tract: {len(stops_with_tract)}")

# sample stops with their tracts income 
print("\nSample stops with their tract's income:")
print(stops_with_tract[["stop_name", "GEOID", "median_income"]].head(5))
stops_with_tract.plot()
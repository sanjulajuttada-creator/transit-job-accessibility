import pandas as pd
import geopandas as gpd
import os

# GTFS data
print("Loading GTFS data...")
stops = pd.read_csv("gtfs/stops.txt")
routes = pd.read_csv("gtfs/routes.txt")
stop_times = pd.read_csv("gtfs/stop_times.txt")

print(f"Stops: {len(stops)} rows")
print(f"Routes: {len(routes)} rows")
print(f"Stop times: {len(stop_times)} rows")

# LODES employment data
print("\nLoading LODES employment data...")
lodes = pd.read_csv("lodes/tx_wac_S000_JT00_2023.csv.gz")
print(f"LODES: {len(lodes)} rows")

# census data
print("\nLoading Census data...")
income = pd.read_csv("census/income_2023.csv")
car_ownership = pd.read_csv("census/carOwnership_2023.csv")
print(f"Income: {len(income)} rows")
print(f"Car ownership: {len(car_ownership)} rows")

# shapefiles
print("\nLoading shapefiles...")
shp_files = [f for f in os.listdir("shapefiles") if f.endswith(".shp")]
print(f"Shapefiles found: {shp_files}")

print("\nData loaded successfully")


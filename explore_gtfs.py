import gtfs_kit as gk

# load the GTFS feed (use distance units in km)
print("Loading DART GTFS feed...")
feed = gk.read_feed("gtfs", dist_units="km")

print("\n--- Agency Info ---")
print(feed.agency[["agency_name", "agency_url"]])

# how many routes, stops, trips there are
print("\n--- Feed Summary ---")
print(f"Number of routes: {len(feed.routes)}")
print(f"Number of stops: {len(feed.stops)}")
print(f"Number of trips: {len(feed.trips)}")

# find available service dates
dates = feed.get_dates()
print(f"\nFeed has {len(dates)} service dates")
print(f"First date: {dates[0]}, Last date: {dates[-1]}")

# from that find the busiest date
busiest_date = feed.compute_busiest_date(dates)
print(f"Busiest service date: {busiest_date}")

trip_stats = feed.compute_trip_stats()
stats = feed.compute_network_stats([busiest_date], trip_stats)
print("\n--- Network Stats for the busiest day ---")
print(stats.T)
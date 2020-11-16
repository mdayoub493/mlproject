from mlproject.distance import haversine
# from ../distance import haversine
# le wagon
lat1, lon1 = 48.865070, 2.380009
#cheng du, china
lat2, lon2 = 30.5728, 100.0668
distance = haversine(lon1, lat1, lon2, lat2)
print(distance)

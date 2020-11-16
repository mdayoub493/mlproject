# -*- coding: UTF-8 -*-
from mlproject.distance import haversine
# from ../distance import haversine


def test_haversine():
    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 48.235, 2.393
    distance = haversine(lon1, lat1, lon2, lat2)    
    assert distance == 70.06711243740715
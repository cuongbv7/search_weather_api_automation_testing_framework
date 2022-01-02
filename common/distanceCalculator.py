import geopy.distance
from robot.api.deco import keyword
from robot.utils.asserts import assert_true


@keyword("coordinate should be accurate within expected value")
def distance_calculator(long1,lat1,long2,lat2, expected):
    coords_1 = (float(lat1),float(long1))
    coords_2 = (float(lat2),float(long2))
    assert_true(geopy.distance.distance(coords_1, coords_2).km <= float(expected),"the coordinate not exactly")





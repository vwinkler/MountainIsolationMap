import mountain
import cartopy.crs as ccrs
from cartopy.geodesic import Geodesic
from shapely.geometry import LineString


class SimpleDominatorFinder:
    def __init__(self, mountains):
        self.mountains = mountains

    def findDominator(self, mountain):
        myGeod = Geodesic()
        def key(m):
            shapelyObject = LineString([(mountain.longtitude, mountain.latitude), (m.longtitude, m.latitude)])
            return myGeod.geometry_length(shapelyObject)
        try:
            return min([m for m in self.mountains if m.elevation > mountain.elevation], key=key)
        except:
            raise ValueError("Mountain has no dominator")

import matplotlib.pyplot as plt
import cartopy.crs as ccrs


class Map:
    def __init__(self):
        self.fig = plt.figure(figsize=(10, 5))
        self.ax = self.fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
        self.ax.set_global()
        self.ax.stock_img()
        self.ax.coastlines()

    def addMountain(self, longtitude, latitude):
        self.ax.plot(longtitude, latitude, '^', transform=ccrs.PlateCarree())

    def addDomination(self, longtitude, latitude, longtitudeDominator, latitudeDominator):
        self.ax.plot([longtitude, longtitudeDominator], [latitude, latitudeDominator], transform=ccrs.PlateCarree())

    def show(self):
        plt.show()

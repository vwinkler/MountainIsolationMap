import pickle
import wikidataDownload
from map import Map

cacheFileName = "mountainsCache.pkl"

def loadMountains():
    return pickle.load(open(cacheFileName, "rb"))

def storeMountains(mountains):
    pickle.dump(mountains, open(cacheFileName, "wb"))

def main():
    try:
        print("Load mountains mountains from cache..")
        mountains = loadMountains()
    except:
        print("Could not load mountains from cache.")
        print("Downloading mountains from Wikidata...")
        mountains = wikidataDownload.loadMountains()
        storeMountains(mountains)

    for mountain in mountains:
        pattern = "{} ({} {}): {} meters"
        print(pattern.format(mountain.name, mountain.latitude, mountain.longtitude, mountain.elevation))
    
    map = Map()
    for mountain in mountains:
        map.addMountain(mountain)
    map.show()


if __name__ == '__main__':
    main()

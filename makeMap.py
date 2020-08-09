import sys
import argparse
import pickle
import wikidataDownload
from map import Map

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--force-download', '-d', action='store_true', dest='forceDownload')
parser.add_argument('--no-download', action='store_true', dest='noDownload')
parser.add_argument('--no-map', action='store_true', dest='noMap')

cacheFileName = "mountainsCache.pkl"

def loadMountains():
    return pickle.load(open(cacheFileName, "rb"))

def storeMountains(mountains):
    pickle.dump(mountains, open(cacheFileName, "wb"))

def downloadAndCacheMountains():
    print("Downloading mountains from Wikidata...")
    mountains = wikidataDownload.loadMountains()
    storeMountains(mountains)
    return mountains

def main():
    args = parser.parse_args()
    mountains = None
    if not args.forceDownload:
        try:
            print("Load mountains mountains from cache...")
            mountains = loadMountains()
        except:
            print("Could not load mountains from cache.")
            if not args.noDownload:
                mountains = downloadAndCacheMountains()
    else:
        mountains = downloadAndCacheMountains()

    if mountains == None:
        sys.stderr.write("Error while trying to load mountains\n")
        return

    for mountain in mountains:
        pattern = "{} ({} {}): {} meters"
        print(pattern.format(mountain.name, mountain.latitude, mountain.longtitude, mountain.elevation))

    if not args.noMap:
        map = Map()
        for mountain in mountains:
            map.addMountain(mountain)
        map.show()


if __name__ == '__main__':
    main()

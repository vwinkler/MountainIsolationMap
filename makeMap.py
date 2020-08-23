import sys
import argparse
import pickle
import json
from wikidataDownload import *
from map import Map
from edgeFinding import *

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--force-download', '-d', action='store_true', dest='forceDownload')
parser.add_argument('--no-download', action='store_true', dest='noDownload')
parser.add_argument('--no-map', action='store_true', dest='noMap')
parser.add_argument('--load-json', '-j', type=str, dest='jsonFile', default=None)

cacheFileName = "mountainsCache.pkl"

def loadMountains():
    return pickle.load(open(cacheFileName, "rb"))

def storeMountains(mountains):
    pickle.dump(mountains, open(cacheFileName, "wb"))

def downloadloadMountains():
    return convertMountains(loadRawDataMountains())

def loadMountainsFromJson(filename):
    print("Loading mountains from '{}'...".format(filename))
    return convertMountains(json.load(open(filename, "rb")))

def downloadMountains():
    print("Downloading mountains from Wikidata...")
    return downloadloadMountains()

def main():
    args = parser.parse_args()
    mountains = None
    if args.forceDownload:
        mountains = downloadMountains()
        storeMountains(mountains)
    elif args.jsonFile is not None:
        mountains = loadMountainsFromJson(args.jsonFile)
    else:
        try:
            print("Load mountains mountains from cache...")
            mountains = loadMountains()
        except:
            print("Could not load mountains from cache.")
            if not args.noDownload:
                mountains = downloadMountains()
                storeMountains(mountains)

    if mountains == None:
        sys.stderr.write("Error while trying to load mountains\n")
        return

    for mountain in mountains:
        pattern = "({} {}): {} meters"
        print(pattern.format(mountain.latitude, mountain.longtitude, mountain.elevation))

    if not args.noMap:
        map = Map()
        for mountain in mountains:
            map.addMountain(mountain.longtitude, mountain.latitude)
        dominationFinder = SimpleDominatorFinder(mountains)
        for mountain in mountains:
            try:
                dominator = dominationFinder.findDominator(mountain)
                pattern = "({} {}): {} meters"
                print(pattern.format(dominator.latitude, dominator.longtitude, dominator.elevation))
                map.addDomination(mountain.longtitude, mountain.latitude, dominator.longtitude, dominator.latitude)
            except ValueError:
                pass
        map.show()


if __name__ == '__main__':
    main()

import wikidataDownload
from map import Map


def main():
    mountains = wikidataDownload.loadMountains()
    for mountain in mountains:
        pattern = "{} ({} {}): {} meters"
        print(pattern.format(mountain.name, mountain.latitude, mountain.longtitude, mountain.elevation))
    map = Map()
    for mountain in mountains:
        map.addMountain(mountain)
    map.show()


if __name__ == '__main__':
    main()

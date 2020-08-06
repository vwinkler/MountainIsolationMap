from qwikidata.sparql import (get_subclasses_of_item,
                              return_sparql_query_results)

import matplotlib.pyplot as plt
import cartopy.crs as ccrs

sparql_query = """
SELECT ?item ?itemLabel ?elevation ?location ?lat ?lon
WHERE 
{
  ?item p:P625 ?location.
  ?item p:P2044/psn:P2044/wikibase:quantityAmount ?elevation .
  ?item wdt:P31 wd:Q8502 ;
  p:P625 [
    psv:P625 [
      wikibase:geoLatitude ?lat ;
      wikibase:geoLongitude ?lon ;
    ] ;
  ].
  FILTER(?elevation > 8000)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 3
"""

res = return_sparql_query_results(sparql_query)
for item in res["results"]["bindings"]:
    print("{} ({} {}): {} meters".format(item["itemLabel"]["value"], item["lat"]["value"], item["lon"]["value"], item["elevation"]["value"]))


def main():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
    ax.set_global()
    ax.stock_img()
    ax.coastlines()

    for item in res["results"]["bindings"]:
        ax.plot(float(item["lon"]["value"]), float(item["lat"]["value"]), '^', transform=ccrs.PlateCarree())

    plt.show()


if __name__ == '__main__':
    main()

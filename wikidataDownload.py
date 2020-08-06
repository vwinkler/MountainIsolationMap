from qwikidata.sparql import (get_subclasses_of_item,
                              return_sparql_query_results)
from mountain import Mountain

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

def loadRawDataMountains():
    res = return_sparql_query_results(sparql_query)
    return res


def convertMountains(wikidataResults):
    mountains = []
    for item in wikidataResults["results"]["bindings"]:
        mountain = Mountain()
        mountain.name = item["itemLabel"]["value"]
        mountain.latitude = float(item["lat"]["value"])
        mountain.longtitude = float(item["lon"]["value"])
        mountain.elevation = float(item["elevation"]["value"])
        mountains.append(mountain)
    return mountains

def loadMountains():
    return convertMountains(loadRawDataMountains())

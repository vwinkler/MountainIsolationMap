from qwikidata.sparql import (get_subclasses_of_item,
                              return_sparql_query_results)
from mountain import Mountain

sparql_query = """
SELECT ?country ?maxElevation ?item ?lon ?lat
{
  {
    SELECT (MAX(?elevation) AS ?maxElevation) ?country
    WHERE
    {
      ?item wdt:P31 wd:Q8502.
      ?item wdt:P17 ?country.
      ?item p:P2044/psn:P2044/wikibase:quantityAmount ?elevation .
    }
  GROUP BY ?country
  }
  
  ?item wdt:P17 ?country.
  ?item p:P2044/psn:P2044/wikibase:quantityAmount ?maxElevation .
  ?item p:P625 ?location.
  ?item wdt:P31 wd:Q8502 ;
        p:P625 [
          psv:P625 [
            wikibase:geoLatitude ?lat ;
            wikibase:geoLongitude ?lon ;
          ] ;
        ].
}
"""

def loadRawDataMountains():
    res = return_sparql_query_results(sparql_query)
    return res


def convertMountains(wikidataResults):
    mountains = []
    for item in wikidataResults["results"]["bindings"]:
        mountain = Mountain()
        mountain.latitude = float(item["lat"]["value"])
        mountain.longtitude = float(item["lon"]["value"])
        mountain.elevation = float(item["maxElevation"]["value"])
        mountains.append(mountain)
    return mountains

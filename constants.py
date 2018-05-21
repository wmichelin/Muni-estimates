BASE_URL = 'http://webservices.nextbus.com/service/publicJSONFeed'
COMMAND_ROUTE_LIST = 'routeList'
COMMAND_PREDICTION = 'predictionsForMultiStops'
AGENCY = 'sf-muni'

N_JUDAH_TAG = 'N'

SIXTEENTH_AND_JUDAH = {
    "routeTag": N_JUDAH_TAG,
    "lon": "-122.4736299",
    "title": "Judah St & 16th Ave",
    "stopId": "15198",
    "tag": "5198",
    "lat": "37.76194"
}

FIFTEENTH_AND_JUDAH = {
    "routeTag": N_JUDAH_TAG,
    "lon": "-122.47278",
    "title": "Judah St & 15th Ave",
    "stopId": "15197",
    "tag": "5197",
    "lat": "37.7618499"
}

DEFAULT_STOPS = [
    SIXTEENTH_AND_JUDAH,
    FIFTEENTH_AND_JUDAH,
]

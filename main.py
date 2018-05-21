import requests

from constants import (
    BASE_URL,
    COMMAND_PREDICTION,
    AGENCY,
    DEFAULT_STOPS
)

def build_prediction_url(stops=DEFAULT_STOPS):
    return (
        BASE_URL + '?' +
        'a=' + AGENCY + '&' +
        'command=' + COMMAND_PREDICTION + '&' +
        build_stops_str(stops)
    )

def build_stops_str(stops=DEFAULT_STOPS):
    stops_str = ''
    for idx, stop in enumerate(stops):
        stops_str += (
            'stops=' +
            stop.get('routeTag') + '|' +
            stop.get('tag')
        )
        if idx is not (len(stops) - 1):
            stops_str += '&'

    return stops_str


def get_predictions():
    url = build_prediction_url()
    return requests.get(url).json().get('predictions')


for result in get_predictions():
    print(result.get('routeTitle'))
    print(result.get('stopTitle'))
    directions = result.get('direction')
    if isinstance(directions, dict): # sometimes it comes back as a single item
        directions = [directions]

    for direction in directions:
        print(direction.get('title'))
        predictions = direction.get('prediction')
        if isinstance(predictions, dict):
            predictions = [predictions]

        for prediction in predictions:
            seconds = float(prediction.get('seconds'))
            minutes = seconds / 60
            print(str(minutes) + ' minutes')
    print('------------------------------------------')
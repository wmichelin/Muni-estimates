from muni import get_predictions

for result in get_predictions():
    print(result.get('routeTitle'))
    print(result.get('stopTitle'))
    directions = result.get('direction')
    if isinstance(directions, dict): # sometimes it comes back as a single item
        directions = [directions]

    if directions:
        for direction in directions:
            print(direction.get('title'))
            predictions = direction.get('prediction')
            if isinstance(predictions, dict):
                predictions = [predictions]

            for prediction in predictions:
                seconds = float(prediction.get('seconds'))
                minutes = round(seconds / 60, 2)
                print(str(minutes) + ' minutes')
    else:
        print('no estimates')
    print('------------------------------------------')
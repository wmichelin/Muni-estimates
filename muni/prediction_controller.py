from muni import get_predictions

class PredictionController:
    def __init__(self):
        pass

    def handle(self):
        predictionResults = []
        for result in get_predictions():
            predictionResult = {
                'lineTitle': result.get('routeTitle'),
                'stopDescription': result.get('stopTitle'),
                'directionResults': [],
            }

            directions = result.get('direction')
            if isinstance(directions, dict): # sometimes it comes back as a single item
                directions = [directions]

            if directions:
                for direction in directions:
                    directionResult = {
                        'directionDescription': direction.get('title'),
                        'estimates': []
                    }

                    predictions = direction.get('prediction')
                    if isinstance(predictions, dict):
                        predictions = [predictions]

                    for prediction in predictions:
                        directionResult.get('estimates').append(float(prediction.get('seconds')) * 1000)

                    predictionResult.get('directionResults').append(directionResult)

            predictionResults.append(predictionResult)

        return predictionResults
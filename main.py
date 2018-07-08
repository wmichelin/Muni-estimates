from muni.prediction_controller import PredictionController
from flask import (
    Flask,
    jsonify,
)
app = Flask(__name__)

@app.route('/')
def get_predictions():
    response = jsonify(PredictionController().handle())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
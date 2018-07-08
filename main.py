from muni.prediction_controller import PredictionController
from flask import (
    Flask,
    jsonify,
)
app = Flask(__name__)

@app.route('/')
def get_predictions():
    return jsonify(PredictionController().handle())
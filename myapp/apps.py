from django.apps import AppConfig
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("decision_tree_model.pkl", "rb"))


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

@flask_app.route("/predict", methods = ["POST"])
def predict():
    print("Hit predict function")
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("prediksi.html", prediction_text = "Customer akan {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)
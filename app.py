from flask import Flask, render_template, url_for, request
import pandas as pd
import os
import pickle

from processing import CategoricalEncoder
from config import FEATURES, CAT_VAR, get_logger


app = Flask(__name__)

_logger = get_logger(logger_name=__name__)


def load_model(model_path):
    pickle_in = open(model_path, 'rb')
    classifier = pickle.load(pickle_in)
    return classifier


def display_result_pred(prediction):
    if prediction == 1:
        display_pred = "You have diabetes"
    else:
        display_pred = "You do not have diabetes"
    return display_pred


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        polyuria = request.form['polyuria']
        polydipsia = request.form['polydipsia']
        sudden_weight_loss = request.form['sudden_weight_loss']
        weakness = request.form['weakness']
        polyphagia = request.form['polyphagia']
        genital_thrush = request.form['genital_thrush']
        visual_blurring = request.form['visual_blurring']
        itching = request.form['itching']
        irritability = request.form['irritability']
        delayed_healing = request.form['delayed_healing']
        partial_paresis = request.form['partial_paresis']
        muscle_stiffness = request.form['muscle_stiffness']
        alopecia = request.form['alopecia']
        obesity = request.form['obesity']

        data = [age, gender, polyuria, polydipsia, sudden_weight_loss, weakness, polyphagia,
                genital_thrush, visual_blurring, itching, irritability, delayed_healing, partial_paresis,
                muscle_stiffness, alopecia, obesity]
        input = pd.DataFrame([data], columns=FEATURES)

        model = load_model('pipeline.pkl')
        prediction = model.predict(input)[0]
        display_pred = display_result_pred(prediction)

        pred_prob = model.predict_proba(input)[0][prediction] * 100

    return render_template('index.html', display_pred=display_pred, pred_prob=pred_prob)


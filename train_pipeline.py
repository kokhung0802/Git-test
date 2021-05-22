import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
import pickle

from processing import CategoricalEncoder
from config import CAT_VAR


df = pd.read_csv(
    'C:/Users/kok19/Desktop/Practice_app/data/train.csv')


pipeline = Pipeline([
    ("categorical_encoder", CategoricalEncoder(variables=CAT_VAR)),
    ("scaler", MinMaxScaler()),
    ("random_forest", RandomForestClassifier())
])

y_df = df['class']
X_df = df.drop('class', axis=1)

y_df = y_df.apply(lambda x: 1 if x == 'Positive' else(
    0 if x == 'Negative' else 'Missing'))

pipeline.fit(X_df, y_df)

# save model
pickle_out = open("pipeline.pkl", "wb")
pickle.dump(pipeline, pickle_out)
pickle_out.close()
print('model saved')

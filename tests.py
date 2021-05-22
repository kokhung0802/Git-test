import pandas as pd
import pickle
from processing import CategoricalEncoder
from config import FEATURES, CAT_VAR, get_logger


_logger = get_logger(logger_name=__name__)


pickle_in = open('pipeline.pkl', 'rb')
classifier = pickle.load(pickle_in)

test_df = pd.read_csv('C:/Users/kok19/Desktop/Diabetes-app/test.csv')

y_df = test_df['class']
X_df = test_df.drop('class', axis=1)

input = X_df.iloc[3:5, :]
_logger.debug(input)

prediction = classifier.predict(input)
_logger.debug(prediction)

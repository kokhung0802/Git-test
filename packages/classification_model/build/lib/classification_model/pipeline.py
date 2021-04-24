from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

from classification_model.processing import preprocessors as pp
from classification_model.config import config


class_pipe = Pipeline(
    [
        (
            "categorical_encoder",
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)
        ),
        ("scaler", MinMaxScaler()),
        ("Random_Forest", RandomForestClassifier())

    ]
)

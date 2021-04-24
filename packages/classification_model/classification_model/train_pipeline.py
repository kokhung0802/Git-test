import numpy as np
from sklearn.model_selection import train_test_split

from classification_model import pipeline
from classification_model.processing.data_management import load_dataset, save_pipeline
from classification_model.config import config


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES], data[config.TARGET], test_size=0.1, random_state=0
    )

    y_train = y_train.apply(lambda x: 1 if x == 'Positive' else(
        0 if x == 'Negative' else 'Missing'))

    pipeline.class_pipe.fit(X_train[config.FEATURES], y_train)

    save_pipeline(pipeline_to_persist=pipeline.class_pipe)


if __name__ == '__main__':
    run_training()

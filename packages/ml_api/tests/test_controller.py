from classification_model.config import config as model_config
from classification_model.processing.data_management import load_dataset
from classification_model import __version__ as _version
from api import __version__ as api_version

import json
import math


def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')

    # Then
    assert response.status_code == 200


def test_version_endpoint_returns_version(flask_test_client):
    # When
    response = flask_test_client.get('/version')

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version


def test_prediction_endpoints_returns_prediction(flask_test_client):
    # Given
    test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)
    post_json = test_data[1:2].to_json(orient='records')

    # When
    response = flask_test_client.post(
        '/v1/predict/classification', json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions'][0]
    response_version = response_json['version']
    assert prediction == 1
    assert response_version == _version

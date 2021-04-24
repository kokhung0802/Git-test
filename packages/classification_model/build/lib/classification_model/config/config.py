import pathlib
import classification_model

PACKAGE_ROOT = pathlib.Path(classification_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "train.csv"
TARGET = "class"

FEATURES = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'Sudden_Weight_Loss', 'Weakness',
            'Polyphagia', 'Genital_Thrush', 'Visual_Blurring', 'Itching', 'Irritability',
            'Delayed_Healing', 'Partial_Paresis', 'Muscle_Stiffness', 'Alopecia', 'Obesity']

CATEGORICAL_VARS = ['Gender', 'Polyuria', 'Polydipsia', 'Sudden_Weight_Loss', 'Weakness',
                    'Polyphagia', 'Genital_Thrush', 'Visual_Blurring', 'Itching', 'Irritability',
                    'Delayed_Healing', 'Partial_Paresis', 'Muscle_Stiffness', 'Alopecia', 'Obesity']

NUMERICAL_VARS = ['Age']

PIPELINE_NAME = "Random_Forest"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05

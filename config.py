import logging
import sys

FEATURES = ['Age', 'Gender', 'Polyuria', 'Polydipsia',
            'sudden weight loss', 'weakness', 'Polyphagia', 'Genital thrush',
            'visual blurring', 'Itching', 'Irritability', 'delayed healing',
            'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity']

CAT_VAR = ['Polyuria', 'Polydipsia',
           'sudden weight loss', 'weakness', 'Polyphagia', 'Genital thrush',
           'visual blurring', 'Itching', 'Irritability', 'delayed healing',
           'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity']


FORMATTER = logging.Formatter(
    "%(asctime)s-%(name)s-%(levelname)s-%(funcName)s:%(lineno)d-%(message)s")


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_logger(*, logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    return logger

from flask import Flask

from test_exam import settings
from test_exam.extensions import db
from test_exam_util.constants import Settings


def create_app(config=None):
    test_exam = Flask(__name__)

    if config is not None:
        configuration = getattr(settings, config + Settings.CONFIG_SUFFIX)
        test_exam.config.from_object(configuration)

    # Registering extensions
    db.init_app(test_exam)

    return test_exam

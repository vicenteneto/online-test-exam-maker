CI_TASKS = (
    'flask_ci.tasks.run_nose',
    'flask_ci.tasks.run_pep8',
    'flask_ci.tasks.run_pylint'
)

VIEWS = ()

PROJECT_APPS = VIEWS + (
    'test_exam',
    'test_exam_users',
    'test_exam_util'
)


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

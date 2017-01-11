CI_TASKS = (
    'flask_ci.tasks.run_nose',
    'flask_ci.tasks.run_pep8',
    'flask_ci.tasks.run_pylint'
)

VIEWS = ()

PROJECT_APPS = VIEWS + (
    'online_test',
    'online_test_users',
    'online_test_util'
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

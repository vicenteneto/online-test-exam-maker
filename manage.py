from flask_ci import CICommand
from flask_script import Manager

from test_exam import app, settings

manager = Manager(app.create_app())
manager.add_command('ci', CICommand(settings))

if __name__ == '__main__':
    manager.run()

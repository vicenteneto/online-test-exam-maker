from flask_ci import CICommand
from flask_script import Manager, Server

from online_test import settings
from online_test.app import create_app
from online_test_util.constants import FlaskScriptCommands, Settings

manager = Manager(create_app)

manager.add_option('-c', '--config', default=Settings.DEVELOPMENT, required=False, dest='config')
manager.add_command(FlaskScriptCommands.CI, CICommand(settings))
manager.add_command(FlaskScriptCommands.RUNSERVER, Server(threaded=True))

if __name__ == '__main__':
    manager.run()

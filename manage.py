#!/usr/bin/env python
"""Creates an application from the configurations provided.
It is the top-level script that runs the application.
"""

import os

from app import create_app, db

from app.models import User, Role

from flask_script import Manager, Shell

from flask_migrate import Migrate, MigrateCommand


# app = create_app(os.getenv('FLASK_CONFIG') or 'default')

app = create_app('development')

manager = Manager(app)

migrate = Migrate(app, db)

def make_shell_context():
    """Inititalizes the custom context for the python shell"""
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
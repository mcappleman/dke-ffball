"""Imports"""
from os import environ
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dke_ffball import app, db

app.config.from_object(environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

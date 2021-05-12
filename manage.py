from exts import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app

import os


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()

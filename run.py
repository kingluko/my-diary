import os

from app import create_app

config_name = os.getenv('APP_SETTING')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()

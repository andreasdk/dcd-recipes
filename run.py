import os
from whisk import create_app
from whisk.config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run(host=os.getenv("IP"), port=os.getenv("PORT"))
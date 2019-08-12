import os
from whisk import app, mongo


if __name__ == '__main__':
    app.run(host=os.getenv("IP"), port=os.getenv("PORT"))
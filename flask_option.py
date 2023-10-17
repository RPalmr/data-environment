# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    flask_env = os.environ.get("FLASK_ENV")

    if flask_env == "development":
        return "Starting in development mode..."
    elif flask_env == "production":
        return "Starting in production mode..."

if __name__ == "__main__":
    print(start())

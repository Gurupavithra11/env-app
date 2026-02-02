import os
from flask import Flask

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "dev")
APP_NAME = os.getenv("APP_NAME", "Config Demo App")

@app.route("/")
def home():
    if APP_ENV == "dev":
        return f"{APP_NAME} running in DEVELOPMENT environment"
    elif APP_ENV == "test":
        return f"{APP_NAME} running in TEST environment"
    else:
        return f"{APP_NAME} running in UNKNOWN environment"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

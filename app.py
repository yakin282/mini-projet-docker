import os
from flask import Flask

app = Flask(__name__)
MESSAGE = os.environ.get("APP_MESSAGE", "Bonjour depuis le conteneur !")

@app.route("/")
def index():
    return MESSAGE + "\n"

app.run(host="0.0.0.0", port=5000)

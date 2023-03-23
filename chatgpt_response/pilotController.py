
from flask import Flask
import os
import sys

CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR + "/..")

from chatgpt_response.pilotService import PilotService

app = Flask(__name__)


@app.route("/ask/<query>")
def ask(query, service=PilotService()):

    return service.ask(query)


if __name__ == '__main__':
    app.run()

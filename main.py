from flask import Flask
from config import Dev, Prod

app = Flask(__name__)


if __name__ == '__main__':
    app.run(host=Dev.HOST, port=Dev.PORT, debug=Dev.DEBUG)

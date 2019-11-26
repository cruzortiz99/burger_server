from flask import Flask
from config import Dev, Prod

app = Flask(__name__)
app.config.from_object(Dev)

if __name__ == '__main__':
    app.run()

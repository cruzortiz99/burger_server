from flask import Flask
from config import Dev, Prod
from src.domain import create_db
from src.routes.user import user_routes
from src.routes.activity import activities_routes

app = Flask(__name__)
create_db()
user_routes(app)
activities_routes(app)

if __name__ == '__main__':
    app.run(host=Dev.HOST, port=Dev.PORT, debug=Dev.DEBUG)

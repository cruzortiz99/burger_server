from flask import Flask
from config import Dev, Prod
from src.routes.user import user_routes
from src.routes.burger import burger_routes

app = Flask(__name__)
app.config.from_object(Dev)

user_routes(app)
burger_routes(app)


if __name__ == '__main__':
    app.run()

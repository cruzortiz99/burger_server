from flask import Flask
from config import Dev, Prod
from src.db import create_db
from src.modules.users.routes.user import router as user_router
from src.modules.events.routes.activity import router as activity_router

create_db()
app = Flask(__name__)
app.register_blueprint(user_router, url_prefix='/')
app.register_blueprint(activity_router, url_prefix='/event')

if __name__ == '__main__':
    app.run(host=Dev.HOST, port=Dev.PORT, debug=Dev.DEBUG)

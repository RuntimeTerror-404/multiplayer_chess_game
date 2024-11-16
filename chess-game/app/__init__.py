# app/__init__.py
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Initialize SocketIO
    socketio.init_app(app)

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app

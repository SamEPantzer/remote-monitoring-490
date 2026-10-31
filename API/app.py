# Create Flask app and register routes

from flask import Flask
from routes import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app

# Run the local development server
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
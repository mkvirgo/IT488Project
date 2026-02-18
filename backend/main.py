from flask import Flask, jsonify, request

import urls
from db import engine
from models import Base


def create_app() -> Flask:
    app = Flask(__name__)

    # Create tables (SQLite) on startup
    Base.metadata.create_all(bind=engine)

    # Register routes/blueprints
    app.register_blueprint(urls.main)

    # Handle preflight OPTIONS cleanly for SPA calls
    @app.before_request
    def handle_options():
        if request.method == "OPTIONS":
            return ("", 204)

    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        return response

    @app.errorhandler(404)
    def not_found(_err):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def server_error(_err):
        return jsonify({"error": "Internal server error"}), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="127.0.0.1", port=5000)



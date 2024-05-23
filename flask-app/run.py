import logging
from app.app import create_app

if __name__ == "__main__":
    try:
        app = create_app()
        app.run(debug=True, host="0.0.0.0", port=8000)
    except Exception as e:
        logging.error("Error running the app: %s", e)

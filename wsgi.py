"""
WSGI entry point for deployment
"""
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app
from backend.app import app

if __name__ == "__main__":
    app.run()


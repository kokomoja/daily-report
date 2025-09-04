#!/bin/bash
# Activate Render's Python virtual environment
source /opt/render/project/.venv/bin/activate

# Run Flask app with gunicorn
gunicorn app:app

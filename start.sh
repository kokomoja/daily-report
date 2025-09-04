#!/bin/bash
source .venv/bin/activate
exec gunicorn app:app --bind 0.0.0.0:$PORT

#!/bin/bash
echo "Starting app with gunicorn..."
exec python3 -m gunicorn app:app --bind 0.0.0.0:10000

#!/bin/bash
echo "Starting app with gunicorn..."
exec gunicorn app:app --bind 0.0.0.0:10000

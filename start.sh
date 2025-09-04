#!/bin/bash
# start.sh
# ใช้สำหรับรัน Flask บน Render ด้วย gunicorn

echo "Starting app with gunicorn..."
gunicorn app:app --bind 0.0.0.0:10000 --workers 4

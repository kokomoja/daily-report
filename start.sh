#!/bin/bash
source /opt/render/project/src/.venv/bin/activate
gunicorn app:app --bind 0.0.0.0:10000

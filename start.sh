#!/bin/bash
# ให้ shell ใช้ virtualenv
source .venv/bin/activate
# สั่งรันด้วย gunicorn
exec gunicorn app:app --bind 0.0.0.0:$PORT

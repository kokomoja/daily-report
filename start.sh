#!/bin/bash

# ใช้ virtual environment ของ Render
VENV_PATH=/opt/render/project/.venv

# Activate venv (ทาง Render บังคับใช้ path ตรง)
source $VENV_PATH/bin/activate

# เริ่ม Flask app ด้วย Gunicorn
$VENV_PATH/bin/gunicorn app:app --bind 0.0.0.0:10000

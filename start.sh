#!/bin/bash

# ติดตั้ง ODBC library และ driver
apt-get update
apt-get install -y unixodbc unixodbc-dev curl
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql17

# ติดตั้ง Python dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# รัน Flask app ด้วย Gunicorn
gunicorn app:app -b 0.0.0.0:$PORT

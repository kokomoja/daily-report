from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime
import pyodbc
import os
from dotenv import load_dotenv

# โหลด .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# สร้าง connection string จาก environment variables
driver = '{ODBC Driver 17 for SQL Server}'
server = os.environ.get("SQL_SERVER")
database = os.environ.get("SQL_DB")
username = os.environ.get("SQL_USER")
password = os.environ.get("SQL_PASSWORD")

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def get_conn():
    return pyodbc.connect(conn_str)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/get-dropdown-data')
def get_dropdown_data():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT machine FROM machineNumber")
    machines = [row.machine for row in cursor.fetchall()]
    cursor.execute("SELECT op_name FROM operatorName")
    operators = [row.op_name for row in cursor.fetchall()]
    conn.close()
    return jsonify({'machines': machines, 'operators': operators})

@app.route('/save-report', methods=['POST'])
def save_report():
    data = request.json
    try:
        op_date = datetime.strptime(data['op_date'], "%Y-%m-%d").date()
        start_time = datetime.strptime(data['start_time'], "%Y-%m-%dT%H:%M")
        stop_time = datetime.strptime(data['stop_time'], "%Y-%m-%dT%H:%M")
        duration = stop_time - start_time
        hours, remainder = divmod(duration.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        op_hour_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

        conn = get_conn()
        cursor = conn.cursor()
        sql = """
        INSERT INTO dailyReport (op_date, machine, operator, job, start_time, stop_time, op_hour)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, data['machine'], data['operator'], data['job'],
                       start_time, stop_time, op_hour_str)
        conn.commit()
        conn.close()
        return jsonify({"message": "บันทึกสำเร็จ!"})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

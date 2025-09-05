from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    # Hardcode dropdown data
    machines = [
        "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
        "Crane Yello", "Crane Blue", "Bobcat", "70-8919",
        "70-8137", "70-6748", "70-8671"
    ]
    operators = [
        "นายอุทัย นามคุณ",
        "นายบัวไข่ วงศ์อำนาจ",
        "นายวิชิต บัวทอง",
        "นายยุทธนา จันทร",
        "นายสนธยา โมคทิพย์",
        "นายชาญชัย ธรรมรักษ์",
        "นายวทัญญู เลิศปรัชญานนท์",
        "นายสมมิตร ช่วยนคร",
        "นายวัชราวุธ เทพหนู",
        "นายเจริญ ขำแก้ว",
        "นายปรีชา ชอบงาม"
    ]
    return render_template("index.html", machines=machines, operators=operators)

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

        print("Report saved:", data)
        return jsonify({"message": "บันทึกสำเร็จ!"})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

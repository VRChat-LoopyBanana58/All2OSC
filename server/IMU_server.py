from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def imu_stream():
    try:
        data = request.get_json()
        if not data:
            return "No JSON received", 400

        # Print the raw JSON for inspection
        print("Received IMU data:")
        for key, value in data.items():
            print(f"{key}: {value}")
        print("-" * 30)

        return jsonify({"status": "ok"})
    except Exception as e:
        print("Error:", e)
        return "Error", 500

if __name__ == '__main__':
    app.run(host='100.80.78.30', port=5000, debug=True)

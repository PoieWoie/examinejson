# app.py
from flask import Flask, request, jsonify
from pprint import pprint  # Import pprint module

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def analyze_json():
    try:
        json_data = request.get_json()

        # Pretty print the incoming JSON data
        print("Incoming JSON data:")
        pprint(json_data)

        return jsonify({"message": "JSON data received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

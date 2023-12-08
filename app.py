from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def analyze_json():
    try:
        # Get JSON data from the request
        json_data = request.get_json()

        # Perform your analysis on the JSON data here
        # For example, you can print the incoming JSON data
        print("Incoming JSON data:", json_data)

        # You can also examine the schema using a library like jsonschema
        # Example: Validate against a schema
        # from jsonschema import validate
        # schema = {"type": "object", "properties": {"key": {"type": "string"}}}
        # validate(json_data, schema)

        # Respond with a success message
        return jsonify({"message": "JSON data received successfully"}), 200
    except Exception as e:
        # Handle any exceptions that may occur
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application on a local development server
    app.run(debug=True)

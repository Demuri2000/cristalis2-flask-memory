from flask import Flask, request, jsonify, send_file
import os
import json

app = Flask(__name__)

MEMORY_FILE = "public_memory.json"

@app.route("/")
def welcome():
    return "🔮 Cristalis2 Memory Server is online."

@app.route("/memory.json", methods=["GET"])
def get_memory():
    if os.path.exists(MEMORY_FILE):
        return send_file(MEMORY_FILE)
    return jsonify({"error": "Memory file not found."}), 404

@app.route("/upload", methods=["POST"])
def upload_memory():
    try:
        content = request.get_json()
        if not content:
            return jsonify({"error": "No JSON received."}), 400

        with open(MEMORY_FILE, "w") as f:
            json.dump(content, f, indent=2)

        return jsonify({"status": "✅ Memory updated successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


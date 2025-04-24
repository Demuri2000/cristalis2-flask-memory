from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

MEMORY_FILE = "public_memory.json"

@app.route("/")
def welcome():
    return "🔮 Cristalis2 Memory Server is online."

@app.route("/memory.json", methods=["GET"])
def get_memory():
    if os.path.exists(MEMORY_FILE):
        return send_file(MEMORY_FILE)
    return jsonify({"error": "Memory not found."}), 404

@app.route("/upload", methods=["POST"])
def upload_memory():
    content = request.get_json()
    if content:
        with open(MEMORY_FILE, "w") as f:
            import json
            json.dump(content, f, indent=2)
        return jsonify({"status": "✅ Memory updated successfully."})
    return jsonify({"error": "No JSON received."}), 400

if __name__ == "__main__":
    app.run(debug=True)


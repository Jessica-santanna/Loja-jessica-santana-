from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "message": "API Jéssica Santana funcionando!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
from core.detector import scan

def launch_dashboard(port=8080):
    app = Flask(__name__)

    @app.route("/api/protect", methods=["POST"])
    def protect():
        payload = request.json.get("input", "")
        result = scan(payload)
        return jsonify(result)

    print(f"[+] Dashboard API running on http://localhost:{port}/api/protect")
    app.run(host="0.0.0.0", port=port)

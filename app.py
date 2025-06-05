from flask import Flask, request, render_template, jsonify
from estimator.ai_estimator import estimate_units
from estimator.cornwall_rules import get_density_rules
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    data = request.get_json()
    polygon = data.get("geometry")
    land_area_m2 = data.get("area_m2")

    if not polygon or not land_area_m2:
        return jsonify({"error": "Missing polygon or area"}), 400

    result = estimate_units(land_area_m2)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
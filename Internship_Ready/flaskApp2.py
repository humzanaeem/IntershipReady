from flask import Flask, jsonify

app = Flask(__name__)

DATA = [
    {"id": 1, "campus": "MMC", "lat": 25.76, "lon": -80.36},
    {"id": 2, "campus": "BBC", "lat": 25.90, "lon": -80.13},
    {"id": 3, "campus": "DC",  "lat": 38.89, "lon": -77.01}
]

@app.route("/")
def index():
    return """
    <h1>FIU Campus API</h1>
    <p>Try these endpoints:</p>
    <ul>
        <li><a href="/api/health">/api/health</a></li>
        <li><a href="/api/items">/api/items</a></li>
        <li><a href="/api/items/1">/api/items/1</a></li>
    </ul>
    """

@app.route("/api/hello")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/data")
def get_items():
    return jsonify(DATA), 200

@app.route("/api/items/<int:item_id>")
def get_item(item_id):
    for item in DATA:
        if item["id"] == item_id:
            return jsonify(item), 200
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5002)

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

from model import predict
from database import init_db

app = Flask(__name__)

# важно: разрешаем CORS полностью (чтобы DELETE/OPTIONS не ломались)
CORS(app, resources={r"/*": {"origins": "*"}})

init_db()


# HOME
@app.route("/")
def home():
    return "AI Server is running"


# ANALYZE
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "No text"}), 400

    text = data["text"].strip()

    result, confidence = predict(text)

    conn = sqlite3.connect("results.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO results (input_text, ai_result, confidence)
        VALUES (?, ?, ?)
    """, (text, result, confidence))

    conn.commit()
    conn.close()

    return jsonify({
        "result": result,
        "confidence": confidence
    })


# HISTORY
@app.route("/results", methods=["GET"])
def results():
    conn = sqlite3.connect("results.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM results ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    return jsonify([
        {
            "id": r["id"],
            "text": r["input_text"],
            "result": r["ai_result"],
            "confidence": r["confidence"],
            "time": r["created_at"]
        }
        for r in rows
    ])


# CLEAR HISTORY (FIXED + OPTIONS SAFE)
@app.route("/clear", methods=["POST", "OPTIONS"])
def clear():

    # если это OPTIONS запрос — просто отвечаем OK
    if request.method == "OPTIONS":
        return jsonify({"ok": True})

    conn = sqlite3.connect("results.db")
    c = conn.cursor()

    c.execute("DELETE FROM results")

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "History cleared"
    })


if __name__ == "__main__":
    app.run(debug=True)

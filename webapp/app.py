from flask import Flask, jsonify
import os, redis

app = Flask(__name__)
db = redis.Redis(host=os.environ.get("REDIS_HOST", "cache_db"), port=6379)

@app.route("/")
def home():
    try:
        req_count = db.incr("api_requests")
    except Exception:
        req_count = "brak polaczenia z baza"
    return f"<h1>Aplikacja Konwertera (Chmura)</h1><p>Liczba zapytan do API: <strong>{req_count}</strong></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

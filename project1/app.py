from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

request_count = Counter('request_count', 'Total number of requests')

@app.route('/')
def home():
    request_count.inc()
    return "Hello, app is running!"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)

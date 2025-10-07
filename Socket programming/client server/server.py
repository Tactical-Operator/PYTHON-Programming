from flask import Flask, request
import logging
import warnings

warnings.filterwarnings("ignore")  # Hide Python warnings
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)  # Hide Flask access logs

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get("message")
    print(f"Client says: {message}")
    return {"status": "received", "message": message}, 200

@app.route('/')
def home():
    return "Flask server is running!"

if __name__ == '__main__':
    app.run(port=5000)

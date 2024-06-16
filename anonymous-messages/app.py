


from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for messages
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    if message:
        messages.append(message)
        return jsonify({"status": "success", "message": "Message received"}), 200
    return jsonify({"status": "error", "message": "No message provided"}), 400

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Changed port to 5001



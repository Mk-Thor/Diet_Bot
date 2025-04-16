from flask import Flask, render_template, request, jsonify
from chatbot import get_chatbot_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mk.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").strip().lower()
    response = get_chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

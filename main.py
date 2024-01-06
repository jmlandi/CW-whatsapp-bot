from assistants import Bruno
from whatsapp import Sandbox, Prd
from flask import Flask, request, jsonify

app = Flask('app')

@app.route('/')
def index():
    return 'API Online'

# SANDBOX ENV // application/x-www-form-urlencoded
@app.route('/direct-messages', methods=['POST'])
def sandbox_messages():
    Sandbox.response(request.form.get('MessageSid'), Bruno.response(request.form.get('Body')))
    return 200

# PRD ENV // application/json
@app.route('/chatbot-workflow', methods=['POST'])
def prd_messages():
    content = request.json
    ai_answer = Bruno.response(content['body'])
    response = {'response': ai_answer}
    return jsonify(response), 200

@app.route('/incoming-message', methods=['POST'])
def incoming_message():
    content = request.data
    print(content)
    return 200

if __name__ == '__main__':
    app.run()
